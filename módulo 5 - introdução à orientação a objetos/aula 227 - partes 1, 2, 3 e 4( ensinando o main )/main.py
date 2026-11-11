# from log import LogFileMixin, LogPrintMixin

# lf = LogFileMixin()
# lf.log_success("Salvo com sucesso no arquivo")
# lf.log_error("Houve um erro ao salvar este arquivo")

# lp = LogPrintMixin()
# lp.log_success("Impressão salva com sucesso")
# lp.log_error("Falha na impressão da mensagem")

from eletronico import Smartphone
galaxy_s = Smartphone('Galaxy S')
iphone = Smartphone('iPhone')

galaxy_s.ligar()
iphone.desligar()