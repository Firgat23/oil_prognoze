from PySide6.QtWidgets import QDialog, QApplication
from forma_3 import Ui_Dialog
import sys
import model_2

app = QApplication(sys.argv)
dialog = QDialog()
ui = Ui_Dialog()
ui.setupUi(dialog)
dialog.show()
ui.Tectonic.addItems(['COMPRESSION','EXTENSION','INVERSION',
'GRAVITY','STRIKE-SLIP','TRANSPRESSION','UPLIFT','TRANSTENSION','EVAPORITE'])
ui.Structural.addItems(['FORELAND','RIFT','SALT','INTRACRATONIC','INVERSION',
'THRUST','DELTA','WRENCH','PASSIVE MARGIN','SUB-SALT','SUB-THRUST','BACKARC'])
ui.Lithology.addItems(['SANDSTONE','LIMESTONE','DOLOMITE','LOW-RESISTIVITY SANDSTONE',
'THINLY-BEDDED SANDSTONE','CHALKY LIMESTONE','CHALK','SHALY SANDSTONE','CONGLOMERATE',
'DOLOMITIC LIMESTONE','SILTSTONE','SHALE','VOLCANICS','GLAUCONITIC SANDSTONE','BASEMENT',
'CHERT','DIATOMITE'])
ui.Type.addItems(['OIL','GAS'])

def foo():
    Type = ui.Type.currentText() or ''
    Tectonic = ui.Tectonic.currentText()
    Lithology = ui.Lithology.currentText()
    Structural = ui.Structural.currentText()
    Gross = int(ui.Gross.toPlainText())
    Netpay = int(ui.Netpay.toPlainText())
    Porosity = int(ui.Porosity.toPlainText())
    Permeability = int(ui.Permeability.toPlainText())
    Depth = int(ui.Depth.toPlainText())
    OilDensity = ui.OilDensity.toPlainText()
    if Type == 'OIL':
        OilDensity = int(OilDensity)
    Nge = Netpay/Gross
    res = model_2.predict(Type,Tectonic,Lithology,Structural,Gross,Netpay,Porosity,Permeability,Depth,OilDensity,Nge)
    ui.result.clear()
    ui.result.setText(str(res))
    

ui.pushButton.clicked.connect(foo)
sys.exit(app.exec())


