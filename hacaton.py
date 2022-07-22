import json

class Cars:
    FILE='jsondb/car.json'
    id=0
    def __init__(self, mark, model, year, obem, color, type_of_kuzov, probeg, price):
        self.mark=mark
        self.model=model
        self.year=year
        self.obem=obem
        self.color=color
        self.type_of_kuzov=type_of_kuzov
        self.probeg=probeg
        self.price=price
        
        self.create()




    @classmethod
    def get_id(cls):
        cls.id+=1
        return cls.id

    @classmethod
    def listing(cls):
        with open(cls.FILE) as file:
            return json.load(file)


    @staticmethod
    def get_one_product(data, id):
        product=list(filter(lambda x: x['id']==id, data))
        if not product:
            return 'NO such product'
        return product[0]

    @classmethod
    def send_data_to_json(cls, data):
        with open(cls.FILE, 'w') as file:
            json.dump(data, file)



    def create(self):
        data=Cars.listing()
        product={

            'id': Cars.get_id(),
            'mark':self.mark,
         'model':self.model, 
         'year':self.year, 
         'obem':self.obem, 
         'color':self.color, 
         'type_of_kuzov':self.type_of_kuzov, 
         'probeg':self.probeg, 
         'price':self.price}
        data.append(product)

        with open (Cars.FILE, 'w') as file:
            json.dump(data, file)
            return {'status':'201', 'msg': product }

    @classmethod
    def retrieve_data(cls, id):
        data=cls.listing()
        product=cls.get_one_product(data, id)
        return product

    @classmethod
    def update_data(cls, id, **kwargs):
        # id=int(input())
        
        data=cls.listing()
        product=cls.get_one_product(data, id)
        if type(product)!=dict:
            return product
        index=data.index(product)
        data[index].update(**kwargs)
        cls.send_data_to_json(data)
        return {'status': '200', 'msg': 'updated'}


    @classmethod
    def delete_data(cls, id):
        data=cls.listing()
        product=cls.get_one_product(data, id)


        if type(product)!=dict:
            return product
        index=data.index(product)
        data.pop(index)
        cls.send_data_to_json(data)
        return {'status':'204', 'msg':'deleted'}
        


with open(Cars.FILE, 'w') as file:
    json.dump([], file)



    


obj1=Cars('Audi', 's1', 2010, 231, 'black', 'hatchback', 'jj', 40000 )
obj2=Cars('BMW', 's1', 2010, 231, 'black', 'hatchback', 'jj', 40000)
obj3=Cars('Acura', 's1', 2010, 231, 'black', 'hatchback', 'jj', 40000)


print('all products:\n', Cars.listing())
print('\n', Cars.retrieve_data(3))
print(Cars.update_data(3, mark='Tayota'))
print('\n', Cars.retrieve_data(3))
print(Cars.delete_data(3))
print('all products:\n', Cars.listing())


    




































