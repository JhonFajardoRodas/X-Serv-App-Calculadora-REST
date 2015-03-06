#!/usr/bin/python

import webapp
import random


class calculadoraREST(webapp.webApp):

    def parse(self, request):
        try:
            metodo =  request.split(' ')[0]
            recurso = request.split()[1][1:]
            if metodo == "PUT":
                cuerpo = request.split('\r\n\r\n',1)[1]
            else:
                cuerpo = ""
        except ValueError:
            return None
        return (metodo, recurso, cuerpo)

    def process(self, parsedRequest):
        (metodo, recurso, cuerpo) = parsedRequest
        if not parsedRequest:
            return ("404 Bad Request", "<html><body><h1>Enter a number!</h1>" +
                    "</body></html>")
        if metodo == "PUT":
            self.operacion = cuerpo
            httpCode = "200 OK"
            htmlBody = "<html><body>" + cuerpo + " Ok!</body></html>"
        elif metodo == "GET":
            operador = self.operacion.split("+")
            if len(operador) == 2:
                operadorOk = "+"
            operador = self.operacion.split("-")
            if len(operador) == 2:
                operadorOk = "-"
            operador = self.operacion.split("*")
            if len(operador) == 2:
                operadorOk = "*"
            operador = self.operacion.split("/")
            if len(operador) == 2:
                operadorOk = "/"
            try:
                num1 = self.operacion.split(operadorOk)[0]
                num2 = self.operacion.split(operadorOk)[1]
                resultado = int(num1) + int(num2)
            except ValueError:
                 return ("404 Bad Request", "<html><body><h1>Enter a number please!</h1>" +
                    "</body></html>")

            httpCode = "200 OK"
            htmlBody = "<html><body>" + self.operacion + " = " + str(resultado) \
                        + "</body></html>"
        return (httpCode, htmlBody)

if __name__ == "__main__":
    testCalculadoraREST = calculadoraREST("localhost", 1234)

