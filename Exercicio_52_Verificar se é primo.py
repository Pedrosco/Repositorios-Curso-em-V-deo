{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Exercicio Python -verificar se é primo",
      "provenance": [],
      "authorship_tag": "ABX9TyNCVGkuJ8udl4eIFqrz5lpz",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Pedrosco/Repositorios-Curso-em-V-deo/blob/main/Exercicio_52_Verificar%20se%20%C3%A9%20primo.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "bL53s7mi6703"
      },
      "source": [
        "numero = float(input('Qual é o número desejado?'))\n",
        "\n",
        "if numero == 2:\n",
        "  print(f'O número {numero} é um número primo')\n",
        "elif numero % 2 == 1:\n",
        "  print(f'O número {numero}, é um número primo')\n",
        "else:\n",
        "  print(f'O número {numero} não é um número primo')\n"
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}