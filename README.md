# Hand-Sensor

> Este é um projeto que utiliza a câmera para detectar e reconhecer mãos, com funcionalidades que permitem identificar a quantidade de dedos levantados e reconhecer gestos simples.

## Índice
- [Introdução](#introdução)
- [Funcionalidades](#funcionalidades)
- [Instalação](#instalação)
- [Uso](#uso)
- [Colaboradores](#colaboradores)
- [Licença](#licença)

## Introdução
Para esse projeto, certifique-se de ter o [Python 3.12 ou superior](https://www.python.org/downloads/) instalado.
Também utilaza-se as bibliotecas listadas abaixo:
- [**OpenCV**](https://docs.opencv.org/4.10.0/): para manipulação de imagens.
- [**MediaPipe**](https://ai.google.dev/edge/mediapipe/solutions/guide): para detecção e rastreamento de mãos.
- [**CVZone**](https://github.com/cvzone/cvzone): para integração fácil entre OpenCV e MediaPipe.

## Funcionalidades

- Detecta uma mão.
- Detecta quantos dedos estão levantados.
- Detecta qual a mão está sendo analisada.
- Dececta alguns gestos simples.

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/gustagt/Hand-Sensor.git
   ```

2. Acesse o diretório do projeto:
   ```bash
   cd Hand-Sensor
   ```
3. Instale as seguinte dependencias.
   ```bash
   pip install opencv-python
   ```
   ```bash
   pip install mediapipe
   ```
   ```bash
   pip install cvzone
   ```

## Uso
 Execute o arquivo app.py dentro do diretorio raiz do projeto Hand-Sensor.
 
  ```bash
  python app.py
  ```


## Colaboradores

As seguintes pessoas que contribuíram para este projeto:

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/gustagt" title="Perfil Gustavo Silva">
        <img src="https://avatars.githubusercontent.com/u/88049338" width="100px;" alt="Foto do Gustavo Silva no GitHub"/><br>
        <sub>
          <b>Gustavo Silva</b>
        </sub>
      </a>
    </td>
  </tr>
</table>

## Licença

Esse projeto está sob licença. Veja o arquivo [LICENÇA](LICENSE) para mais detalhes.
   
