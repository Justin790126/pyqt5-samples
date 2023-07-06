from DisplayProduct.DisplayProductView import DisplayProductView
from DisplayProduct.DisplayProductModel import DisplayProductModel

class DisplayProductCtrller():
    def __init__(self, productId):

        self.productId = productId
        self.model = DisplayProductModel()
        self.view = DisplayProductView(self.productId)

        ##############################

        self.view.uploadBtn.clicked.connect(self.view.uploadImg)
        self.view.updateBtn.clicked.connect(self.view.updateProduct)
        self.view.deleteBtn.clicked.connect(self.view.deleteProduct)
        
        ##############################

        self.model.initDataPrepareDone.connect(self.view.setInitDatas)
        self.model.prepareDatas(self.productId)

        self.view.updateUI2DB.connect(self.update2DB)
        self.model.updateDBresult.connect(self.view.showUpdateDBresult)

        self.view.delete2DB.connect(self.delete2DB)
        self.model.deleteDBresult.connect(self.view.showUpdateDBresult)


    def update2DB(self, queryArgs):
        self.model.updateData2DB(queryArgs)

    def delete2DB(self, productId):
        self.model.deleteBy(productId)
        
    

      