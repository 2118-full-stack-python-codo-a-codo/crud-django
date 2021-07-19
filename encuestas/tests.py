from django.test import TestCase

# Create your tests here.

class MyIntegrationTest(TestCase):

    def setUp(self) -> None:
        '''
            Inicializa el set de pruebas.
        '''
        return super().setUp()
    
    def testHelloWrold(self):
        response = self.client.get("/users/")
        self.assertContains(response , "Hello world from Django for Codo a Codo 4.0")

    def testSatusCodeHelloWorld(self):
        response = self.client.get("/users/")
        self.assertEqual(response.status_code, 200 )
     
     def testProbarUrlJhonathan(self):
        response = self.client.get("/jhonathan/")
        self.assertContains(response , "Test aceptado y creado por Jhonathan Peña")

    #Testing the CRUD
    def testCreate(self):
        self.fail()

    def testUpdate(self):
        self.fail()

    def testDelete(self):
        self.fail()

    def testRead(self):
        self.fail()
    
