# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_editor.ui'
#
# Created: Sun Mar 27 14:11:15 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MetatoolsEditor(object):
    def setupUi(self, MetatoolsEditor):
        MetatoolsEditor.setObjectName(_fromUtf8("MetatoolsEditor"))
        MetatoolsEditor.resize(800, 600)
        MetatoolsEditor.setSizeGripEnabled(True)
        self.verticalLayout = QtGui.QVBoxLayout(MetatoolsEditor)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtGui.QTabWidget(MetatoolsEditor)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.splitter = QtGui.QSplitter(self.tab)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setOpaqueResize(True)
        self.splitter.setHandleWidth(5)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.treeView = QtGui.QTreeView(self.splitter)
        self.treeView.setAnimated(True)
        self.treeView.setObjectName(_fromUtf8("treeView"))
        self.editorGroupBox = QtGui.QGroupBox(self.splitter)
        self.editorGroupBox.setEnabled(False)
        self.editorGroupBox.setObjectName(_fromUtf8("editorGroupBox"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.editorGroupBox)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.nodePathLabel = QtGui.QLabel(self.editorGroupBox)
        self.nodePathLabel.setText(_fromUtf8(""))
        self.nodePathLabel.setWordWrap(True)
        self.nodePathLabel.setObjectName(_fromUtf8("nodePathLabel"))
        self.verticalLayout_2.addWidget(self.nodePathLabel)
        self.valueTextEdit = QtGui.QTextEdit(self.editorGroupBox)
        self.valueTextEdit.setObjectName(_fromUtf8("valueTextEdit"))
        self.verticalLayout_2.addWidget(self.valueTextEdit)
        self.valueButtonBox = QtGui.QDialogButtonBox(self.editorGroupBox)
        self.valueButtonBox.setStandardButtons(QtGui.QDialogButtonBox.Apply|QtGui.QDialogButtonBox.Discard)
        self.valueButtonBox.setObjectName(_fromUtf8("valueButtonBox"))
        self.verticalLayout_2.addWidget(self.valueButtonBox)
        self.verticalLayout_3.addWidget(self.splitter)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.splitter_2 = QtGui.QSplitter(self.tab_2)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setOpaqueResize(True)
        self.splitter_2.setHandleWidth(5)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.filterTreeView = QtGui.QTreeView(self.splitter_2)
        self.filterTreeView.setAnimated(True)
        self.filterTreeView.setObjectName(_fromUtf8("filterTreeView"))
        self.filterEditorGroupBox = QtGui.QGroupBox(self.splitter_2)
        self.filterEditorGroupBox.setEnabled(False)
        self.filterEditorGroupBox.setObjectName(_fromUtf8("filterEditorGroupBox"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.filterEditorGroupBox)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.filterNodePathLabel = QtGui.QLabel(self.filterEditorGroupBox)
        self.filterNodePathLabel.setText(_fromUtf8(""))
        self.filterNodePathLabel.setWordWrap(True)
        self.filterNodePathLabel.setObjectName(_fromUtf8("filterNodePathLabel"))
        self.verticalLayout_4.addWidget(self.filterNodePathLabel)
        self.filterValueTextEdit = QtGui.QTextEdit(self.filterEditorGroupBox)
        self.filterValueTextEdit.setObjectName(_fromUtf8("filterValueTextEdit"))
        self.verticalLayout_4.addWidget(self.filterValueTextEdit)
        self.filterValueButtonBox = QtGui.QDialogButtonBox(self.filterEditorGroupBox)
        self.filterValueButtonBox.setStandardButtons(QtGui.QDialogButtonBox.Apply|QtGui.QDialogButtonBox.Discard)
        self.filterValueButtonBox.setObjectName(_fromUtf8("filterValueButtonBox"))
        self.verticalLayout_4.addWidget(self.filterValueButtonBox)
        self.verticalLayout_5.addWidget(self.splitter_2)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        self.mainButtonBox = QtGui.QDialogButtonBox(MetatoolsEditor)
        self.mainButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.mainButtonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Save)
        self.mainButtonBox.setObjectName(_fromUtf8("mainButtonBox"))
        self.verticalLayout.addWidget(self.mainButtonBox)

        self.retranslateUi(MetatoolsEditor)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MetatoolsEditor)

    def retranslateUi(self, MetatoolsEditor):
        MetatoolsEditor.setWindowTitle(QtGui.QApplication.translate("MetatoolsEditor", "Metadata editor", None, QtGui.QApplication.UnicodeUTF8))
        self.editorGroupBox.setTitle(QtGui.QApplication.translate("MetatoolsEditor", "Edit value", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("MetatoolsEditor", "Full view", None, QtGui.QApplication.UnicodeUTF8))
        self.filterEditorGroupBox.setTitle(QtGui.QApplication.translate("MetatoolsEditor", "Edit value", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("MetatoolsEditor", "Filtered view", None, QtGui.QApplication.UnicodeUTF8))

