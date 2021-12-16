import addressbook_pb2

person = addressbook_pb2.Person()
person.id = 1234
person.name = "David Kyungil Kim"
person.email = "jdoe@example.com"
phone = person.phones.add()
phone.number = "010-2222-1111"
phone.type = addressbook_pb2.Person.MOBILE

with open('out.txt', 'wb') as f:
    f.write(person.SerializeToString())

with open('out.txt', 'rb') as f:
    read_metric = addressbook_pb2.Person()
    read_metric.ParseFromString(f.read())
    print(read_metric)
