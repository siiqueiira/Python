def unip():
        reverso = {11:'A', 12:'B', 13:'C', 14:'D', 15:'E', 16:'F',
                21:'G', 22:'H', 23:'I', 24:'J', 25:'K', 26:'L',
                31:'M', 32:'N', 33:'O', 34:'P', 35:'Q', 36:'R',
                41:'S', 42:'T', 43:'U', 44:'V', 45:'W', 46:'X',
                51:'Y', 52:'Z', 53:'0', 54:'1', 55:'2', 56:'3',
                61:'4', 62:'5', 63:'6', 64:'7', 65:'8', 66:'9'}


        mensagem = int(input('Digite a mensagem a ser DESCRIPTOGRAFADA:'))

        mensagem2 = int(input('Digite a mensagem a ser DESCRIPTOGRAFADA:'))

        mensagem3 = int(input('Digite a mensagem a ser DESCRIPTOGRAFADA:'))

        mensagem4 = int(input('Digite a mensagem a ser DESCRIPTOGRAFADA:'))

        mensagem5 = int(input('Digite a mensagem a ser DESCRIPTOGRAFADA:'))

        descripto1 = " "
        descripto2 = " "
        descripto3 = " "
        descripto4 = " "
        descripto5 = " "

        for teste in reverso:
                descripto1 = reverso[mensagem]

        for teste in reverso:
                descripto2 = reverso[mensagem2]

        for teste in reverso:
                descripto3 = reverso[mensagem3]

        for teste in reverso:
                descripto4 = reverso[mensagem4]

        for teste in reverso:
                descripto5 = reverso[mensagem5]

        print(f'Mensagem Descriptografada: {descripto1+descripto2+descripto3+descripto4+descripto5}')