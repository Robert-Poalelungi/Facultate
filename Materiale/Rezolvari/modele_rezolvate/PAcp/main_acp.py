import sys
import PySide2.QtWidgets as qw
import acp

if __name__ == '__main__':
    app = qw.QApplication(sys.argv)
    m_acp = acp.acp()
    m_acp.form.show()
    sys.exit(app.exec_())
