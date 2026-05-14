class cafetera:
    def preparar_cafe(self):
        self._hervir_agua()
        self._moler_cafe()
        print("Café listo!")

    def _hervir_agua(self):
        print("Hirviendo agua")

    def _moler_cafe(self):
        print("Molendo café")

def main():
    mi_cafetera = cafetera()
    cafetera.preparar_cafe()

if __name__ == "__main__":
    main()