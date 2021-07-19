from django.test import TestCase

# Create your tests here.

class MyIntegrationTest(TestCase):

    def setUp(self) -> None:
        '''
            Inicializa el set de pruebas.
        '''
        return super().setUp()
    
    def testHelloWorld(self):
        response = self.client.get("/users/")
        self.assertContains(response , "Hello world from Django for Codo a Codo 4.0")

    def testStatusCodeHelloWorld(self):
        response = self.client.get("/users/")
        self.assertEqual(response.status_code, 200 )

    def testProbarUrlLeo(self):
        response = self.client.get("/leonardo/")
        self.assertContains(response , "Test aceptado y creado por Leonardo Guzman")
        #test agregado por Leonardo


    #Testing the CRUD
    def testCreate(self):
        self.fail()

    def testUpdate(self):
        self.fail()

    def testDelete(self):
        self.fail()

    def testRead(self):
        self.fail()
    