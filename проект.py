   def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.lastPoint = event.pos()

    def mouseMoveEvent(self, event):
        if (event.buttons() & Qt.LeftButton) & self.drawing:
            painter = QPainter(self.image)
            painter.setPen(QPen(self.brushColor, self.brushSize, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
            painter.drawLine(self.lastPoint, event.pos())
            self.lastPoint = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button == Qt.LeftButton:
            self.drawing = False

    def paintEvent(self, event):
        canvasPainter = QPainter(self)
        canvasPainter.drawImage(self.rect(), self.image, self.image.rect())

    def save(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save Image", "",
                                                  "PNG(*.png);;JPEG(*.jpg *.jpeg);; ALL Files(*.*)")
        if filePath == "":
            return
        self.image.save(filePath)

    # TODO
    def openfile(self):
        filePath, _ = QFileDialog.getOpenFileName(self, "Open Image", "",
                                                  "PNG(*.png);;JPEG(*.jpg *.jpeg);; ALL Files(*.*)")
        if filePath == "":
            return
        self.image.load(filePath)
        self.update()

    def clear(self):
        self.image.fill(Qt.white)
        self.update()

    def threePx(self):
        self.brushSize = 3

    def fivePx(self):
        self.brushSize = 5

    def sevenPx(self):
        self.brushSize = 7

    def ninePx(self):
        self.brushSize = 9

    def blackColo(self):
        self.brushColor = Qt.black

    def redColo(self):
        self.brushColor = Qt.red

    def greenColo(self):
        self.brushColor = Qt.green

    def yellowColo(self):
        self.brushColor = Qt.yellow

    def palitraColor(self):
        selectedcolor = QColorDialog.getColor()
        self.brushColor = selectedcolor

    def eraser(self):
        self.brushColor = Qt.white
        self.brushSize = 5


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec()