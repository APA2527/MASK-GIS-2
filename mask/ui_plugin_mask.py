# Form implementation generated from reading ui file 'W:\GitHub\mask\mask\ui_plugin_mask.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets


class Ui_MainDialog(object):
    def setupUi(self, MainDialog):
        MainDialog.setObjectName("MainDialog")
        MainDialog.resize(695, 779)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(MainDialog)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox = QtWidgets.QGroupBox(MainDialog)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.stylePreview = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stylePreview.sizePolicy().hasHeightForWidth())
        self.stylePreview.setSizePolicy(sizePolicy)
        self.stylePreview.setFrameShape(QtWidgets.QFrame.Box)
        self.stylePreview.setLineWidth(1)
        self.stylePreview.setMidLineWidth(0)
        self.stylePreview.setText("")
        self.stylePreview.setObjectName("stylePreview")
        self.horizontalLayout_4.addWidget(self.stylePreview)
        self.editStyleBtn = QtWidgets.QPushButton(self.groupBox)
        self.editStyleBtn.setObjectName("editStyleBtn")
        self.horizontalLayout_4.addWidget(self.editStyleBtn)
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_4.addItem(spacerItem)
        self.verticalLayout_4.addWidget(self.groupBox)
        self.bufferGroup = QtWidgets.QGroupBox(MainDialog)
        self.bufferGroup.setFlat(False)
        self.bufferGroup.setCheckable(True)
        self.bufferGroup.setChecked(False)
        self.bufferGroup.setObjectName("bufferGroup")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.bufferGroup)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.bufferGroup)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.bufferUnits = QtWidgets.QLineEdit(self.bufferGroup)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bufferUnits.sizePolicy().hasHeightForWidth())
        self.bufferUnits.setSizePolicy(sizePolicy)
        self.bufferUnits.setObjectName("bufferUnits")
        self.horizontalLayout_3.addWidget(self.bufferUnits)
        self.label_4 = QtWidgets.QLabel(self.bufferGroup)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.bufferSegments = QtWidgets.QLineEdit(self.bufferGroup)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.bufferSegments.sizePolicy().hasHeightForWidth()
        )
        self.bufferSegments.setSizePolicy(sizePolicy)
        self.bufferSegments.setObjectName("bufferSegments")
        self.horizontalLayout_3.addWidget(self.bufferSegments)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout_4.addWidget(self.bufferGroup)
        self.simplifyGroup = QtWidgets.QGroupBox(MainDialog)
        self.simplifyGroup.setCheckable(True)
        self.simplifyGroup.setChecked(True)
        self.simplifyGroup.setObjectName("simplifyGroup")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.simplifyGroup)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.simplifyGroup)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.simplifyTolerance = QtWidgets.QLineEdit(self.simplifyGroup)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.simplifyTolerance.sizePolicy().hasHeightForWidth()
        )
        self.simplifyTolerance.setSizePolicy(sizePolicy)
        self.simplifyTolerance.setObjectName("simplifyTolerance")
        self.horizontalLayout_5.addWidget(self.simplifyTolerance)
        self.label_3 = QtWidgets.QLabel(self.simplifyGroup)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.verticalLayout_4.addWidget(self.simplifyGroup)
        self.labelingGroup = QtWidgets.QGroupBox(MainDialog)
        self.labelingGroup.setCheckable(False)
        self.labelingGroup.setChecked(False)
        self.labelingGroup.setObjectName("labelingGroup")
        self.labelingLayout = QtWidgets.QVBoxLayout(self.labelingGroup)
        self.labelingLayout.setObjectName("labelingLayout")
        self.verticalLayout_4.addWidget(self.labelingGroup)
        self.saveLayerGroup = QtWidgets.QGroupBox(MainDialog)
        self.saveLayerGroup.setCheckable(True)
        self.saveLayerGroup.setChecked(False)
        self.saveLayerGroup.setObjectName("saveLayerGroup")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.saveLayerGroup)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.filePath = QtWidgets.QLineEdit(self.saveLayerGroup)
        self.filePath.setObjectName("filePath")
        self.horizontalLayout.addWidget(self.filePath)
        self.browseBtn = QtWidgets.QPushButton(self.saveLayerGroup)
        self.browseBtn.setObjectName("browseBtn")
        self.horizontalLayout.addWidget(self.browseBtn)
        self.formatLbl = QtWidgets.QLabel(self.saveLayerGroup)
        self.formatLbl.setObjectName("formatLbl")
        self.horizontalLayout.addWidget(self.formatLbl)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_4.addWidget(self.saveLayerGroup)
        spacerItem1 = QtWidgets.QSpacerItem(
            20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_4.addItem(spacerItem1)
        self.buttonBox = QtWidgets.QDialogButtonBox(MainDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(
            QtWidgets.QDialogButtonBox.Apply
            | QtWidgets.QDialogButtonBox.Cancel
            | QtWidgets.QDialogButtonBox.Help
            | QtWidgets.QDialogButtonBox.Ok
        )
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_4.addWidget(self.buttonBox)

        self.retranslateUi(MainDialog)
        self.buttonBox.accepted.connect(MainDialog.accept)
        self.buttonBox.rejected.connect(MainDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(MainDialog)

    def retranslateUi(self, MainDialog):
        _translate = QtCore.QCoreApplication.translate
        MainDialog.setWindowTitle(_translate("MainDialog", "Define a mask"))
        self.groupBox.setToolTip(
            _translate("MainDialog", "Style to use for mask layer")
        )
        self.groupBox.setTitle(_translate("MainDialog", "Style"))
        self.editStyleBtn.setText(_translate("MainDialog", "Edit"))
        self.bufferGroup.setToolTip(
            _translate("MainDialog", "Buffer around the mask geometry")
        )
        self.bufferGroup.setTitle(_translate("MainDialog", "Buffer"))
        self.label_2.setText(_translate("MainDialog", "Units"))
        self.label_4.setText(_translate("MainDialog", "Segments"))
        self.bufferSegments.setText(_translate("MainDialog", "5"))
        self.simplifyGroup.setToolTip(
            _translate(
                "MainDialog",
                "On-the-fly simplification used for the mask geometry used in expressions ($mask_geometry)",
            )
        )
        self.simplifyGroup.setTitle(
            _translate("MainDialog", "On-the-fly simplification")
        )
        self.label_5.setText(_translate("MainDialog", "Tolerance"))
        self.simplifyTolerance.setText(_translate("MainDialog", "1.0"))
        self.label_3.setText(_translate("MainDialog", "pixels"))
        self.labelingGroup.setToolTip(
            _translate(
                "MainDialog",
                "If a layer is checked here, its labeling options will be modified in order that its labels will be only visible from inside the mask's polygon",
            )
        )
        self.labelingGroup.setTitle(
            _translate("MainDialog", "Limit labeling to mask's polygon")
        )
        self.saveLayerGroup.setToolTip(
            _translate(
                "MainDialog",
                "Whether the save the mask layer. By default a memory layer is created",
            )
        )
        self.saveLayerGroup.setTitle(_translate("MainDialog", "Save as"))
        self.browseBtn.setText(_translate("MainDialog", "..."))
        self.formatLbl.setText(_translate("MainDialog", "''"))
