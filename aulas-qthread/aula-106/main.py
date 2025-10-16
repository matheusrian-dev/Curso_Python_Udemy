from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import QObject, Signal, QThread
from ui_workerui import Ui_my_widget
import sys
import time

"""
Threads são linhas de execução dentro do programa
São como mini tarefas que o sistema executa em paralelo
com outras tarefas do mesmo programa.

Detalhe importante:
Em programas com interfaces gráficas, tudo que altera
a interface deve ser feito apenas pela thread principal,
enquanto o processamento robusto roda nas threads
secundárias. Por isso o Qt utiliza signals para comunicar
o resultado de uma thread de volta para a thread principal.
"""


class Worker1(QObject):
    started = Signal(str)
    progressed = Signal(str)
    finished = Signal(str)

    def run(self):
        value = '0'
        self.started.emit(value)
        for i in range(5):
            value = str(i)
            self.progressed.emit(value)
            time.sleep(1)
        self.finished.emit(value)


class MyWidget(QWidget, Ui_my_widget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.pushButton_1.clicked.connect(self.hard_work_1)
        self.pushButton_2.clicked.connect(self.hard_work_2)

    def hard_work_1(self):
        self._worker = Worker1()
        self._thread = QThread()
        # Garante que o widget vai ter uma referência para worker e
        # thread.
        worker = self._worker
        thread = self._thread

        # Mova o worker para thread
        worker.moveToThread(thread)

        # Conecte ao método run
        thread.started.connect(worker.run)

        # Após finalizar o método run, finalize a thread
        worker.finished.connect(thread.quit)

        # Garante que irá remover os objetos da memória após
        # o worker finalizar a tarefa.
        thread.finished.connect(thread.deleteLater)
        worker.finished.connect(worker.deleteLater)

        worker.started.connect(self.worker_1_started)
        worker.progressed.connect(self.worker_1_progressed)
        worker.finished.connect(self.worker_1_finished)

        thread.start()

    def worker_1_started(self, value):
        self.pushButton_1.setDisabled(True)
        self.label_1.setText(value)
        print('worker 1 iniciado')

    def worker_1_progressed(self, value):
        self.label_1.setText(value)
        print('worker 1 em progresso')

    def worker_1_finished(self, value):
        self.pushButton_1.setDisabled(False)
        self.label_1.setText(value)
        print('worker 1 finalizado')

    def hard_work_2(self):
        self._worker_2 = Worker1()
        self._thread_2 = QThread()

        worker = self._worker
        thread = self._thread

        # Mova o worker para thread
        worker.moveToThread(thread)

        # Conecte ao método run
        thread.started.connect(worker.run)

        # Após finalizar o método run, finalize a thread
        worker.finished.connect(thread.quit)

        # Garante que irá remover os dados da memória
        thread.finished.connect(thread.deleteLater)
        worker.finished.connect(worker.deleteLater)

        worker.started.connect(self.worker_2_started)
        worker.progressed.connect(self.worker_2_progressed)
        worker.finished.connect(self.worker_2_finished)

        thread.start()

    def worker_2_started(self, value):
        self.pushButton_2.setDisabled(True)
        self.label_2.setText(value)
        print('worker 2 iniciado')

    def worker_2_progressed(self, value):
        self.label_2.setText(value)
        print('worker 2 em progresso')

    def worker_2_finished(self, value):
        self.pushButton_2.setDisabled(False)
        self.label_2.setText(value)
        print('worker 2 finalizado')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_widget = MyWidget()
    my_widget.show()
    app.exec()
