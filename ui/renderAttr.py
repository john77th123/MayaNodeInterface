# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'renderAttr.ui'
#
# Created: Sat Mar 10 14:36:06 2012
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_renderAttr(object):
    def setupUi(self, renderAttr):
        renderAttr.setObjectName("renderAttr")
        renderAttr.resize(323, 361)
        self.gridLayout_11 = QtGui.QGridLayout(renderAttr)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.particleRenderTypeLabel = QtGui.QLabel(renderAttr)
        self.particleRenderTypeLabel.setObjectName("particleRenderTypeLabel")
        self.gridLayout_11.addWidget(self.particleRenderTypeLabel, 0, 0, 1, 1)
        self.particleRenderType = QtGui.QComboBox(renderAttr)
        self.particleRenderType.setObjectName("particleRenderType")
        self.particleRenderType.addItem("")
        self.particleRenderType.addItem("")
        self.particleRenderType.addItem("")
        self.particleRenderType.addItem("")
        self.particleRenderType.addItem("")
        self.particleRenderType.addItem("")
        self.particleRenderType.addItem("")
        self.particleRenderType.addItem("")
        self.particleRenderType.addItem("")
        self.particleRenderType.addItem("")
        self.gridLayout_11.addWidget(self.particleRenderType, 1, 0, 1, 1)
        self.renderTypeWidget = QtGui.QStackedWidget(renderAttr)
        self.renderTypeWidget.setFrameShape(QtGui.QFrame.Panel)
        self.renderTypeWidget.setFrameShadow(QtGui.QFrame.Sunken)
        self.renderTypeWidget.setObjectName("renderTypeWidget")
        self.multiPointPage = QtGui.QWidget()
        self.multiPointPage.setObjectName("multiPointPage")
        self.gridLayout = QtGui.QGridLayout(self.multiPointPage)
        self.gridLayout.setObjectName("gridLayout")
        self.colorAccumulationMP = QtGui.QCheckBox(self.multiPointPage)
        self.colorAccumulationMP.setObjectName("colorAccumulationMP")
        self.gridLayout.addWidget(self.colorAccumulationMP, 0, 0, 1, 2)
        self.multiCountMPLabel = QtGui.QLabel(self.multiPointPage)
        self.multiCountMPLabel.setObjectName("multiCountMPLabel")
        self.gridLayout.addWidget(self.multiCountMPLabel, 1, 0, 1, 1)
        self.multiCountMP = QtGui.QSpinBox(self.multiPointPage)
        self.multiCountMP.setMaximum(1000000000)
        self.multiCountMP.setProperty("value", 8)
        self.multiCountMP.setObjectName("multiCountMP")
        self.gridLayout.addWidget(self.multiCountMP, 1, 1, 1, 1)
        self.multiRadiusMPLabel = QtGui.QLabel(self.multiPointPage)
        self.multiRadiusMPLabel.setObjectName("multiRadiusMPLabel")
        self.gridLayout.addWidget(self.multiRadiusMPLabel, 2, 0, 1, 1)
        self.multiRadiusMP = QtGui.QDoubleSpinBox(self.multiPointPage)
        self.multiRadiusMP.setMaximum(1000000000.0)
        self.multiRadiusMP.setProperty("value", 1.0)
        self.multiRadiusMP.setObjectName("multiRadiusMP")
        self.gridLayout.addWidget(self.multiRadiusMP, 2, 1, 1, 1)
        self.normalDirMPLabel = QtGui.QLabel(self.multiPointPage)
        self.normalDirMPLabel.setObjectName("normalDirMPLabel")
        self.gridLayout.addWidget(self.normalDirMPLabel, 3, 0, 1, 1)
        self.normalDirMP = QtGui.QSpinBox(self.multiPointPage)
        self.normalDirMP.setMaximum(3)
        self.normalDirMP.setProperty("value", 2)
        self.normalDirMP.setObjectName("normalDirMP")
        self.gridLayout.addWidget(self.normalDirMP, 3, 1, 1, 1)
        self.pointSizeMPLabel = QtGui.QLabel(self.multiPointPage)
        self.pointSizeMPLabel.setObjectName("pointSizeMPLabel")
        self.gridLayout.addWidget(self.pointSizeMPLabel, 4, 0, 1, 1)
        self.pointSizeMP = QtGui.QSpinBox(self.multiPointPage)
        self.pointSizeMP.setMaximum(1000000000)
        self.pointSizeMP.setProperty("value", 1)
        self.pointSizeMP.setObjectName("pointSizeMP")
        self.gridLayout.addWidget(self.pointSizeMP, 4, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 5, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 3, 2, 1, 1)
        self.renderTypeWidget.addWidget(self.multiPointPage)
        self.multiStreakPage = QtGui.QWidget()
        self.multiStreakPage.setObjectName("multiStreakPage")
        self.gridLayout_2 = QtGui.QGridLayout(self.multiStreakPage)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.colorAccumulationMS = QtGui.QCheckBox(self.multiStreakPage)
        self.colorAccumulationMS.setObjectName("colorAccumulationMS")
        self.gridLayout_2.addWidget(self.colorAccumulationMS, 0, 0, 1, 2)
        self.lineWidthMSLabel = QtGui.QLabel(self.multiStreakPage)
        self.lineWidthMSLabel.setObjectName("lineWidthMSLabel")
        self.gridLayout_2.addWidget(self.lineWidthMSLabel, 1, 0, 1, 1)
        self.lineWidthMS = QtGui.QSpinBox(self.multiStreakPage)
        self.lineWidthMS.setMaximum(1000000000)
        self.lineWidthMS.setProperty("value", 1)
        self.lineWidthMS.setObjectName("lineWidthMS")
        self.gridLayout_2.addWidget(self.lineWidthMS, 1, 1, 1, 1)
        self.multiCountMSLabel = QtGui.QLabel(self.multiStreakPage)
        self.multiCountMSLabel.setObjectName("multiCountMSLabel")
        self.gridLayout_2.addWidget(self.multiCountMSLabel, 2, 0, 1, 1)
        self.multiCountMS = QtGui.QSpinBox(self.multiStreakPage)
        self.multiCountMS.setMaximum(1000000000)
        self.multiCountMS.setProperty("value", 8)
        self.multiCountMS.setObjectName("multiCountMS")
        self.gridLayout_2.addWidget(self.multiCountMS, 2, 1, 1, 1)
        self.multiRadiusMSLabel = QtGui.QLabel(self.multiStreakPage)
        self.multiRadiusMSLabel.setObjectName("multiRadiusMSLabel")
        self.gridLayout_2.addWidget(self.multiRadiusMSLabel, 3, 0, 1, 1)
        self.multiRadiusMS = QtGui.QDoubleSpinBox(self.multiStreakPage)
        self.multiRadiusMS.setMaximum(1000000000.0)
        self.multiRadiusMS.setProperty("value", 1.0)
        self.multiRadiusMS.setObjectName("multiRadiusMS")
        self.gridLayout_2.addWidget(self.multiRadiusMS, 3, 1, 1, 1)
        self.normalDirMSLabel = QtGui.QLabel(self.multiStreakPage)
        self.normalDirMSLabel.setObjectName("normalDirMSLabel")
        self.gridLayout_2.addWidget(self.normalDirMSLabel, 4, 0, 1, 1)
        self.normalDirMS = QtGui.QSpinBox(self.multiStreakPage)
        self.normalDirMS.setMaximum(3)
        self.normalDirMS.setProperty("value", 2)
        self.normalDirMS.setObjectName("normalDirMS")
        self.gridLayout_2.addWidget(self.normalDirMS, 4, 1, 1, 1)
        self.tailFadeMSLabel = QtGui.QLabel(self.multiStreakPage)
        self.tailFadeMSLabel.setObjectName("tailFadeMSLabel")
        self.gridLayout_2.addWidget(self.tailFadeMSLabel, 5, 0, 1, 1)
        self.tailFadeMS = QtGui.QDoubleSpinBox(self.multiStreakPage)
        self.tailFadeMS.setMaximum(1000000000.0)
        self.tailFadeMS.setProperty("value", 1.0)
        self.tailFadeMS.setObjectName("tailFadeMS")
        self.gridLayout_2.addWidget(self.tailFadeMS, 5, 1, 1, 1)
        self.tailSizeMSLabel = QtGui.QLabel(self.multiStreakPage)
        self.tailSizeMSLabel.setObjectName("tailSizeMSLabel")
        self.gridLayout_2.addWidget(self.tailSizeMSLabel, 6, 0, 1, 1)
        self.tailSizeMS = QtGui.QDoubleSpinBox(self.multiStreakPage)
        self.tailSizeMS.setMaximum(1000000000.0)
        self.tailSizeMS.setProperty("value", 1.0)
        self.tailSizeMS.setObjectName("tailSizeMS")
        self.gridLayout_2.addWidget(self.tailSizeMS, 6, 1, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 2, 2, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem3, 7, 1, 1, 1)
        self.renderTypeWidget.addWidget(self.multiStreakPage)
        self.numericPage = QtGui.QWidget()
        self.numericPage.setObjectName("numericPage")
        self.gridLayout_3 = QtGui.QGridLayout(self.numericPage)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.attributeNameNumLabel = QtGui.QLabel(self.numericPage)
        self.attributeNameNumLabel.setObjectName("attributeNameNumLabel")
        self.gridLayout_3.addWidget(self.attributeNameNumLabel, 0, 0, 1, 1)
        self.attributeNameNum = QtGui.QLineEdit(self.numericPage)
        self.attributeNameNum.setObjectName("attributeNameNum")
        self.gridLayout_3.addWidget(self.attributeNameNum, 0, 1, 1, 1)
        self.pointSizeNumLabel = QtGui.QLabel(self.numericPage)
        self.pointSizeNumLabel.setObjectName("pointSizeNumLabel")
        self.gridLayout_3.addWidget(self.pointSizeNumLabel, 1, 0, 1, 1)
        self.pointSizeNum = QtGui.QSpinBox(self.numericPage)
        self.pointSizeNum.setMinimum(1)
        self.pointSizeNum.setMaximum(1000000000)
        self.pointSizeNum.setObjectName("pointSizeNum")
        self.gridLayout_3.addWidget(self.pointSizeNum, 1, 1, 1, 1)
        self.selectedOnlyNum = QtGui.QCheckBox(self.numericPage)
        self.selectedOnlyNum.setObjectName("selectedOnlyNum")
        self.gridLayout_3.addWidget(self.selectedOnlyNum, 2, 0, 1, 2)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem4, 0, 2, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem5, 3, 0, 1, 1)
        self.renderTypeWidget.addWidget(self.numericPage)
        self.pointsPage = QtGui.QWidget()
        self.pointsPage.setObjectName("pointsPage")
        self.gridLayout_4 = QtGui.QGridLayout(self.pointsPage)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.colorAccumulationPoints = QtGui.QCheckBox(self.pointsPage)
        self.colorAccumulationPoints.setObjectName("colorAccumulationPoints")
        self.gridLayout_4.addWidget(self.colorAccumulationPoints, 0, 0, 1, 2)
        self.normalDirPointsLabel = QtGui.QLabel(self.pointsPage)
        self.normalDirPointsLabel.setObjectName("normalDirPointsLabel")
        self.gridLayout_4.addWidget(self.normalDirPointsLabel, 1, 0, 1, 1)
        self.normalDirPoints = QtGui.QSpinBox(self.pointsPage)
        self.normalDirPoints.setMaximum(3)
        self.normalDirPoints.setProperty("value", 2)
        self.normalDirPoints.setObjectName("normalDirPoints")
        self.gridLayout_4.addWidget(self.normalDirPoints, 1, 1, 1, 1)
        self.pointSizePointsLabel = QtGui.QLabel(self.pointsPage)
        self.pointSizePointsLabel.setObjectName("pointSizePointsLabel")
        self.gridLayout_4.addWidget(self.pointSizePointsLabel, 2, 0, 1, 1)
        self.pointSizePoints = QtGui.QSpinBox(self.pointsPage)
        self.pointSizePoints.setMaximum(1000000000)
        self.pointSizePoints.setProperty("value", 1)
        self.pointSizePoints.setObjectName("pointSizePoints")
        self.gridLayout_4.addWidget(self.pointSizePoints, 2, 1, 1, 1)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem6, 1, 2, 1, 1)
        spacerItem7 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem7, 3, 1, 1, 1)
        self.renderTypeWidget.addWidget(self.pointsPage)
        self.spheresPage = QtGui.QWidget()
        self.spheresPage.setObjectName("spheresPage")
        self.gridLayout_5 = QtGui.QGridLayout(self.spheresPage)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.radiusSphereLabel = QtGui.QLabel(self.spheresPage)
        self.radiusSphereLabel.setObjectName("radiusSphereLabel")
        self.gridLayout_5.addWidget(self.radiusSphereLabel, 0, 0, 1, 1)
        self.radiusSphere = QtGui.QDoubleSpinBox(self.spheresPage)
        self.radiusSphere.setDecimals(3)
        self.radiusSphere.setMaximum(1000000000.0)
        self.radiusSphere.setObjectName("radiusSphere")
        self.gridLayout_5.addWidget(self.radiusSphere, 0, 1, 1, 1)
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem8, 0, 2, 1, 1)
        spacerItem9 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem9, 1, 1, 1, 1)
        self.renderTypeWidget.addWidget(self.spheresPage)
        self.spritesPage = QtGui.QWidget()
        self.spritesPage.setObjectName("spritesPage")
        self.gridLayout_6 = QtGui.QGridLayout(self.spritesPage)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.spriteNumLabel = QtGui.QLabel(self.spritesPage)
        self.spriteNumLabel.setObjectName("spriteNumLabel")
        self.gridLayout_6.addWidget(self.spriteNumLabel, 0, 0, 1, 1)
        self.spriteNum = QtGui.QSpinBox(self.spritesPage)
        self.spriteNum.setMaximum(1000000000)
        self.spriteNum.setObjectName("spriteNum")
        self.gridLayout_6.addWidget(self.spriteNum, 0, 1, 1, 1)
        self.spriteScaleXLabel = QtGui.QLabel(self.spritesPage)
        self.spriteScaleXLabel.setObjectName("spriteScaleXLabel")
        self.gridLayout_6.addWidget(self.spriteScaleXLabel, 1, 0, 1, 1)
        self.spriteScaleX = QtGui.QDoubleSpinBox(self.spritesPage)
        self.spriteScaleX.setDecimals(3)
        self.spriteScaleX.setMaximum(1000000000.0)
        self.spriteScaleX.setProperty("value", 1.0)
        self.spriteScaleX.setObjectName("spriteScaleX")
        self.gridLayout_6.addWidget(self.spriteScaleX, 1, 1, 1, 1)
        self.spriteScaleYLabel = QtGui.QLabel(self.spritesPage)
        self.spriteScaleYLabel.setObjectName("spriteScaleYLabel")
        self.gridLayout_6.addWidget(self.spriteScaleYLabel, 2, 0, 1, 1)
        self.spriteScaleY = QtGui.QDoubleSpinBox(self.spritesPage)
        self.spriteScaleY.setDecimals(3)
        self.spriteScaleY.setMaximum(1000000000.0)
        self.spriteScaleY.setProperty("value", 1.0)
        self.spriteScaleY.setObjectName("spriteScaleY")
        self.gridLayout_6.addWidget(self.spriteScaleY, 2, 1, 1, 1)
        self.spriteTwistLabel = QtGui.QLabel(self.spritesPage)
        self.spriteTwistLabel.setObjectName("spriteTwistLabel")
        self.gridLayout_6.addWidget(self.spriteTwistLabel, 3, 0, 1, 1)
        self.spriteTwist = QtGui.QDoubleSpinBox(self.spritesPage)
        self.spriteTwist.setDecimals(3)
        self.spriteTwist.setMaximum(1000000000.0)
        self.spriteTwist.setProperty("value", 0.0)
        self.spriteTwist.setObjectName("spriteTwist")
        self.gridLayout_6.addWidget(self.spriteTwist, 3, 1, 1, 1)
        spacerItem10 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem10, 4, 1, 1, 1)
        spacerItem11 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem11, 2, 2, 1, 1)
        self.renderTypeWidget.addWidget(self.spritesPage)
        self.streakPage = QtGui.QWidget()
        self.streakPage.setObjectName("streakPage")
        self.gridLayout_7 = QtGui.QGridLayout(self.streakPage)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.lineWidthStreakLabel = QtGui.QLabel(self.streakPage)
        self.lineWidthStreakLabel.setObjectName("lineWidthStreakLabel")
        self.gridLayout_7.addWidget(self.lineWidthStreakLabel, 0, 0, 1, 1)
        self.lineWidthStreak = QtGui.QSpinBox(self.streakPage)
        self.lineWidthStreak.setMaximum(1000000000)
        self.lineWidthStreak.setProperty("value", 1)
        self.lineWidthStreak.setObjectName("lineWidthStreak")
        self.gridLayout_7.addWidget(self.lineWidthStreak, 0, 1, 1, 1)
        self.normalDirStreakLabel = QtGui.QLabel(self.streakPage)
        self.normalDirStreakLabel.setObjectName("normalDirStreakLabel")
        self.gridLayout_7.addWidget(self.normalDirStreakLabel, 1, 0, 1, 1)
        self.normalDirStreak = QtGui.QSpinBox(self.streakPage)
        self.normalDirStreak.setMaximum(3)
        self.normalDirStreak.setProperty("value", 2)
        self.normalDirStreak.setObjectName("normalDirStreak")
        self.gridLayout_7.addWidget(self.normalDirStreak, 1, 1, 1, 1)
        self.tailFadeStreakLabel = QtGui.QLabel(self.streakPage)
        self.tailFadeStreakLabel.setObjectName("tailFadeStreakLabel")
        self.gridLayout_7.addWidget(self.tailFadeStreakLabel, 2, 0, 1, 1)
        self.tailFadeStreak = QtGui.QDoubleSpinBox(self.streakPage)
        self.tailFadeStreak.setMaximum(1000000000.0)
        self.tailFadeStreak.setProperty("value", 1.0)
        self.tailFadeStreak.setObjectName("tailFadeStreak")
        self.gridLayout_7.addWidget(self.tailFadeStreak, 2, 1, 1, 1)
        self.tailSizeStreakLabel = QtGui.QLabel(self.streakPage)
        self.tailSizeStreakLabel.setObjectName("tailSizeStreakLabel")
        self.gridLayout_7.addWidget(self.tailSizeStreakLabel, 3, 0, 1, 1)
        self.tailSizeStreak = QtGui.QDoubleSpinBox(self.streakPage)
        self.tailSizeStreak.setMaximum(1000000000.0)
        self.tailSizeStreak.setProperty("value", 1.0)
        self.tailSizeStreak.setObjectName("tailSizeStreak")
        self.gridLayout_7.addWidget(self.tailSizeStreak, 3, 1, 1, 1)
        spacerItem12 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem12, 4, 1, 1, 1)
        spacerItem13 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem13, 3, 2, 1, 1)
        self.renderTypeWidget.addWidget(self.streakPage)
        self.blobbyPage = QtGui.QWidget()
        self.blobbyPage.setObjectName("blobbyPage")
        self.gridLayout_8 = QtGui.QGridLayout(self.blobbyPage)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.radiusBlobbyLabel = QtGui.QLabel(self.blobbyPage)
        self.radiusBlobbyLabel.setObjectName("radiusBlobbyLabel")
        self.gridLayout_8.addWidget(self.radiusBlobbyLabel, 0, 0, 1, 1)
        self.radiusBlobby = QtGui.QDoubleSpinBox(self.blobbyPage)
        self.radiusBlobby.setDecimals(3)
        self.radiusBlobby.setMaximum(1000000000.0)
        self.radiusBlobby.setProperty("value", 1.0)
        self.radiusBlobby.setObjectName("radiusBlobby")
        self.gridLayout_8.addWidget(self.radiusBlobby, 0, 1, 1, 1)
        self.thresholdLabel = QtGui.QLabel(self.blobbyPage)
        self.thresholdLabel.setObjectName("thresholdLabel")
        self.gridLayout_8.addWidget(self.thresholdLabel, 1, 0, 1, 1)
        self.thresholdBlobby = QtGui.QDoubleSpinBox(self.blobbyPage)
        self.thresholdBlobby.setDecimals(3)
        self.thresholdBlobby.setMaximum(1000000000.0)
        self.thresholdBlobby.setObjectName("thresholdBlobby")
        self.gridLayout_8.addWidget(self.thresholdBlobby, 1, 1, 1, 1)
        spacerItem14 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem14, 0, 2, 1, 1)
        spacerItem15 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_8.addItem(spacerItem15, 2, 1, 1, 1)
        self.renderTypeWidget.addWidget(self.blobbyPage)
        self.cloudPage = QtGui.QWidget()
        self.cloudPage.setObjectName("cloudPage")
        self.gridLayout_9 = QtGui.QGridLayout(self.cloudPage)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.betterIlluminationCloud = QtGui.QCheckBox(self.cloudPage)
        self.betterIlluminationCloud.setObjectName("betterIlluminationCloud")
        self.gridLayout_9.addWidget(self.betterIlluminationCloud, 0, 0, 1, 3)
        self.radiusCloudLabel = QtGui.QLabel(self.cloudPage)
        self.radiusCloudLabel.setObjectName("radiusCloudLabel")
        self.gridLayout_9.addWidget(self.radiusCloudLabel, 1, 0, 1, 1)
        self.radiusCloud = QtGui.QDoubleSpinBox(self.cloudPage)
        self.radiusCloud.setDecimals(3)
        self.radiusCloud.setMaximum(1000000000.0)
        self.radiusCloud.setProperty("value", 1.0)
        self.radiusCloud.setObjectName("radiusCloud")
        self.gridLayout_9.addWidget(self.radiusCloud, 1, 1, 1, 2)
        self.surfaceShadingCloudLabel = QtGui.QLabel(self.cloudPage)
        self.surfaceShadingCloudLabel.setObjectName("surfaceShadingCloudLabel")
        self.gridLayout_9.addWidget(self.surfaceShadingCloudLabel, 2, 0, 1, 2)
        self.surfaceShadingCloud = QtGui.QDoubleSpinBox(self.cloudPage)
        self.surfaceShadingCloud.setDecimals(3)
        self.surfaceShadingCloud.setMaximum(1000000000.0)
        self.surfaceShadingCloud.setObjectName("surfaceShadingCloud")
        self.gridLayout_9.addWidget(self.surfaceShadingCloud, 2, 2, 1, 1)
        self.thresholdCloudLabel = QtGui.QLabel(self.cloudPage)
        self.thresholdCloudLabel.setObjectName("thresholdCloudLabel")
        self.gridLayout_9.addWidget(self.thresholdCloudLabel, 3, 0, 1, 1)
        self.thresholdCloud = QtGui.QDoubleSpinBox(self.cloudPage)
        self.thresholdCloud.setDecimals(3)
        self.thresholdCloud.setMaximum(1000000000.0)
        self.thresholdCloud.setObjectName("thresholdCloud")
        self.gridLayout_9.addWidget(self.thresholdCloud, 3, 1, 1, 2)
        spacerItem16 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem16, 1, 3, 1, 1)
        spacerItem17 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_9.addItem(spacerItem17, 4, 1, 1, 1)
        self.renderTypeWidget.addWidget(self.cloudPage)
        self.tubePage = QtGui.QWidget()
        self.tubePage.setObjectName("tubePage")
        self.gridLayout_10 = QtGui.QGridLayout(self.tubePage)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.radius0TubeLabel = QtGui.QLabel(self.tubePage)
        self.radius0TubeLabel.setObjectName("radius0TubeLabel")
        self.gridLayout_10.addWidget(self.radius0TubeLabel, 0, 0, 1, 1)
        self.radius0Tube = QtGui.QDoubleSpinBox(self.tubePage)
        self.radius0Tube.setDecimals(3)
        self.radius0Tube.setMaximum(1000000000.0)
        self.radius0Tube.setObjectName("radius0Tube")
        self.gridLayout_10.addWidget(self.radius0Tube, 0, 1, 1, 1)
        self.radius1TubeLabel = QtGui.QLabel(self.tubePage)
        self.radius1TubeLabel.setObjectName("radius1TubeLabel")
        self.gridLayout_10.addWidget(self.radius1TubeLabel, 1, 0, 1, 1)
        self.radius1Tube = QtGui.QDoubleSpinBox(self.tubePage)
        self.radius1Tube.setDecimals(3)
        self.radius1Tube.setMaximum(1000000000.0)
        self.radius1Tube.setObjectName("radius1Tube")
        self.gridLayout_10.addWidget(self.radius1Tube, 1, 1, 1, 1)
        self.tailSizeTubeLabel = QtGui.QLabel(self.tubePage)
        self.tailSizeTubeLabel.setObjectName("tailSizeTubeLabel")
        self.gridLayout_10.addWidget(self.tailSizeTubeLabel, 2, 0, 1, 1)
        self.tailSizeTube = QtGui.QDoubleSpinBox(self.tubePage)
        self.tailSizeTube.setDecimals(3)
        self.tailSizeTube.setMaximum(1000000000.0)
        self.tailSizeTube.setObjectName("tailSizeTube")
        self.gridLayout_10.addWidget(self.tailSizeTube, 2, 1, 1, 1)
        spacerItem18 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_10.addItem(spacerItem18, 3, 0, 1, 1)
        spacerItem19 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem19, 2, 2, 1, 1)
        self.renderTypeWidget.addWidget(self.tubePage)
        self.gridLayout_11.addWidget(self.renderTypeWidget, 2, 0, 1, 1)
        spacerItem20 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_11.addItem(spacerItem20, 2, 1, 1, 1)
        self.depthSort = QtGui.QCheckBox(renderAttr)
        self.depthSort.setObjectName("depthSort")
        self.gridLayout_11.addWidget(self.depthSort, 3, 0, 1, 1)
        self.useLighting = QtGui.QCheckBox(renderAttr)
        self.useLighting.setObjectName("useLighting")
        self.gridLayout_11.addWidget(self.useLighting, 4, 0, 1, 1)
        spacerItem21 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_11.addItem(spacerItem21, 5, 0, 1, 2)

        self.retranslateUi(renderAttr)
        self.particleRenderType.setCurrentIndex(3)
        self.renderTypeWidget.setCurrentIndex(3)
        QtCore.QObject.connect(self.particleRenderType, QtCore.SIGNAL("currentIndexChanged(int)"), self.renderTypeWidget.setCurrentIndex)
        QtCore.QMetaObject.connectSlotsByName(renderAttr)

    def retranslateUi(self, renderAttr):
        renderAttr.setWindowTitle(QtGui.QApplication.translate("renderAttr", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.particleRenderTypeLabel.setText(QtGui.QApplication.translate("renderAttr", "Particle Render Type:", None, QtGui.QApplication.UnicodeUTF8))
        self.particleRenderType.setItemText(0, QtGui.QApplication.translate("renderAttr", "MultiPoint", None, QtGui.QApplication.UnicodeUTF8))
        self.particleRenderType.setItemText(1, QtGui.QApplication.translate("renderAttr", "MultiStreak", None, QtGui.QApplication.UnicodeUTF8))
        self.particleRenderType.setItemText(2, QtGui.QApplication.translate("renderAttr", "Numeric", None, QtGui.QApplication.UnicodeUTF8))
        self.particleRenderType.setItemText(3, QtGui.QApplication.translate("renderAttr", "Points", None, QtGui.QApplication.UnicodeUTF8))
        self.particleRenderType.setItemText(4, QtGui.QApplication.translate("renderAttr", "Spheres", None, QtGui.QApplication.UnicodeUTF8))
        self.particleRenderType.setItemText(5, QtGui.QApplication.translate("renderAttr", "Sprites", None, QtGui.QApplication.UnicodeUTF8))
        self.particleRenderType.setItemText(6, QtGui.QApplication.translate("renderAttr", "Streak", None, QtGui.QApplication.UnicodeUTF8))
        self.particleRenderType.setItemText(7, QtGui.QApplication.translate("renderAttr", "Blobby Surface", None, QtGui.QApplication.UnicodeUTF8))
        self.particleRenderType.setItemText(8, QtGui.QApplication.translate("renderAttr", "Cloud", None, QtGui.QApplication.UnicodeUTF8))
        self.particleRenderType.setItemText(9, QtGui.QApplication.translate("renderAttr", "Tube", None, QtGui.QApplication.UnicodeUTF8))
        self.colorAccumulationMP.setText(QtGui.QApplication.translate("renderAttr", "Color Accumulation", None, QtGui.QApplication.UnicodeUTF8))
        self.multiCountMPLabel.setText(QtGui.QApplication.translate("renderAttr", "Multi Count", None, QtGui.QApplication.UnicodeUTF8))
        self.multiRadiusMPLabel.setText(QtGui.QApplication.translate("renderAttr", "Multi Radius", None, QtGui.QApplication.UnicodeUTF8))
        self.normalDirMPLabel.setText(QtGui.QApplication.translate("renderAttr", "Normal Dir", None, QtGui.QApplication.UnicodeUTF8))
        self.pointSizeMPLabel.setText(QtGui.QApplication.translate("renderAttr", "Point Size", None, QtGui.QApplication.UnicodeUTF8))
        self.colorAccumulationMS.setText(QtGui.QApplication.translate("renderAttr", "Color Accumulation", None, QtGui.QApplication.UnicodeUTF8))
        self.lineWidthMSLabel.setText(QtGui.QApplication.translate("renderAttr", "Line Width", None, QtGui.QApplication.UnicodeUTF8))
        self.multiCountMSLabel.setText(QtGui.QApplication.translate("renderAttr", "Multi Count", None, QtGui.QApplication.UnicodeUTF8))
        self.multiRadiusMSLabel.setText(QtGui.QApplication.translate("renderAttr", "Multi Radius", None, QtGui.QApplication.UnicodeUTF8))
        self.normalDirMSLabel.setText(QtGui.QApplication.translate("renderAttr", "Normal Dir", None, QtGui.QApplication.UnicodeUTF8))
        self.tailFadeMSLabel.setText(QtGui.QApplication.translate("renderAttr", "Tail Fade", None, QtGui.QApplication.UnicodeUTF8))
        self.tailSizeMSLabel.setText(QtGui.QApplication.translate("renderAttr", "Tail Size", None, QtGui.QApplication.UnicodeUTF8))
        self.attributeNameNumLabel.setText(QtGui.QApplication.translate("renderAttr", "Attribute Name", None, QtGui.QApplication.UnicodeUTF8))
        self.pointSizeNumLabel.setText(QtGui.QApplication.translate("renderAttr", "Point Size", None, QtGui.QApplication.UnicodeUTF8))
        self.selectedOnlyNum.setText(QtGui.QApplication.translate("renderAttr", "Selected Only", None, QtGui.QApplication.UnicodeUTF8))
        self.colorAccumulationPoints.setText(QtGui.QApplication.translate("renderAttr", "Color Accumulation", None, QtGui.QApplication.UnicodeUTF8))
        self.normalDirPointsLabel.setText(QtGui.QApplication.translate("renderAttr", "Normal Dir", None, QtGui.QApplication.UnicodeUTF8))
        self.pointSizePointsLabel.setText(QtGui.QApplication.translate("renderAttr", "Point Size", None, QtGui.QApplication.UnicodeUTF8))
        self.radiusSphereLabel.setText(QtGui.QApplication.translate("renderAttr", "Radius", None, QtGui.QApplication.UnicodeUTF8))
        self.spriteNumLabel.setText(QtGui.QApplication.translate("renderAttr", "Sprite Num", None, QtGui.QApplication.UnicodeUTF8))
        self.spriteScaleXLabel.setText(QtGui.QApplication.translate("renderAttr", "Sprite Scale X", None, QtGui.QApplication.UnicodeUTF8))
        self.spriteScaleYLabel.setText(QtGui.QApplication.translate("renderAttr", "Sprite Scale Y", None, QtGui.QApplication.UnicodeUTF8))
        self.spriteTwistLabel.setText(QtGui.QApplication.translate("renderAttr", "Sprite Twist", None, QtGui.QApplication.UnicodeUTF8))
        self.lineWidthStreakLabel.setText(QtGui.QApplication.translate("renderAttr", "Line Width", None, QtGui.QApplication.UnicodeUTF8))
        self.normalDirStreakLabel.setText(QtGui.QApplication.translate("renderAttr", "Normal Dir", None, QtGui.QApplication.UnicodeUTF8))
        self.tailFadeStreakLabel.setText(QtGui.QApplication.translate("renderAttr", "Tail Fade", None, QtGui.QApplication.UnicodeUTF8))
        self.tailSizeStreakLabel.setText(QtGui.QApplication.translate("renderAttr", "Tail Size", None, QtGui.QApplication.UnicodeUTF8))
        self.radiusBlobbyLabel.setText(QtGui.QApplication.translate("renderAttr", "Radius", None, QtGui.QApplication.UnicodeUTF8))
        self.thresholdLabel.setText(QtGui.QApplication.translate("renderAttr", "Threshold", None, QtGui.QApplication.UnicodeUTF8))
        self.betterIlluminationCloud.setText(QtGui.QApplication.translate("renderAttr", "Better Illumination", None, QtGui.QApplication.UnicodeUTF8))
        self.radiusCloudLabel.setText(QtGui.QApplication.translate("renderAttr", "Radius", None, QtGui.QApplication.UnicodeUTF8))
        self.surfaceShadingCloudLabel.setText(QtGui.QApplication.translate("renderAttr", "Surface Shading", None, QtGui.QApplication.UnicodeUTF8))
        self.thresholdCloudLabel.setText(QtGui.QApplication.translate("renderAttr", "Threshold", None, QtGui.QApplication.UnicodeUTF8))
        self.radius0TubeLabel.setText(QtGui.QApplication.translate("renderAttr", "Radius 0", None, QtGui.QApplication.UnicodeUTF8))
        self.radius1TubeLabel.setText(QtGui.QApplication.translate("renderAttr", "Radius 1", None, QtGui.QApplication.UnicodeUTF8))
        self.tailSizeTubeLabel.setText(QtGui.QApplication.translate("renderAttr", "Tail Size", None, QtGui.QApplication.UnicodeUTF8))
        self.depthSort.setText(QtGui.QApplication.translate("renderAttr", "Depth Sort", None, QtGui.QApplication.UnicodeUTF8))
        self.useLighting.setText(QtGui.QApplication.translate("renderAttr", "Use Lighting", None, QtGui.QApplication.UnicodeUTF8))

