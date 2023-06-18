{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
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
      "source": [
        "Q1. Create one variable containing following type of data:\n",
        "(i) string\n",
        "(ii) list\n",
        "(iii) float\n",
        "(iv) tuple"
      ],
      "metadata": {
        "id": "Pt9-G3_vPhTU"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "a= 'abcd'\n",
        "print(type(a))\n",
        "b=['a','b',7,8,9j]\n",
        "print(type(b))\n",
        "print(type(b[3]))\n",
        "c= 4.5\n",
        "print(type(c))\n",
        "d= (1,2,3,56,7)\n",
        "print(type(d))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "GWlnz8lVPjmy",
        "outputId": "35ab4493-7f80-4c64-c1b1-382d5fb24ae0"
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'str'>\n",
            "<class 'list'>\n",
            "<class 'int'>\n",
            "<class 'float'>\n",
            "<class 'tuple'>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Q2. Given are some following variables containing data:\n",
        "(i) var1 = ‘ ‘\n",
        "(ii) var2 = ‘[ DS , ML , Python]’\n",
        "(iii) var3 = [ ‘DS’ , ’ML’ , ‘Python’ ]\n",
        "(iv) var4 = 1."
      ],
      "metadata": {
        "id": "F38bfGfNQRL8"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "var1 = ''\n",
        "print(type(var1))\n",
        "var2 = '[ DS, ML , Python]'\n",
        "print(type(var2))\n",
        "var3 = [ 'DS' , 'ML' , 'Python' ]\n",
        "print(type(var3))\n",
        "var4 = 1.\n",
        "print(type(var4))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "xDGS_p_zQb8a",
        "outputId": "8d59ab0f-ebd6-45a5-934d-fefcbf58d3a2"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'str'>\n",
            "<class 'str'>\n",
            "<class 'list'>\n",
            "<class 'float'>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Q3. Explain the use of the following operators using an example:\n",
        "(i) /\n",
        "(ii) %\n",
        "(iii) //\n",
        "(iv) **"
      ],
      "metadata": {
        "id": "6m1WnzQ8RCsL"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "print(7/2) #diveder gives exact value\n",
        "print(7%2) #remainder\n",
        "print(7//2) #this func is also used to divide but in this we get a int instead of float it removes value after .\n",
        "print(7**2)# 7 to the power of 2"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "CO1Q8SAlRDxa",
        "outputId": "13f63c12-2b40-4c89-d1b1-2a0cc3d2e8f2"
      },
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "3.5\n",
            "1\n",
            "3\n",
            "49\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Q4. Create a list of length 10 of your choice containing multiple types of data. Using for loop print the\n",
        "element and its data type."
      ],
      "metadata": {
        "id": "Wl0WY5ibSHky"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "raj= ['a','b',3,3.5,5j,2,'c','raj','yo','whatsup']\n",
        "print(len(raj))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "O9VujbEOSDk7",
        "outputId": "399c408d-ddc4-4c25-a976-0ae63481c1c5"
      },
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "10\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "for i in raj:\n",
        "  print(i,type(i))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "-QFfHUIRSD_8",
        "outputId": "4306a267-72e6-476c-e40f-03b570d9184a"
      },
      "execution_count": 21,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "a <class 'str'>\n",
            "b <class 'str'>\n",
            "3 <class 'int'>\n",
            "3.5 <class 'float'>\n",
            "5j <class 'complex'>\n",
            "2 <class 'int'>\n",
            "c <class 'str'>\n",
            "raj <class 'str'>\n",
            "yo <class 'str'>\n",
            "whatsup <class 'str'>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Q5. Using a while loop, verify if the number A is purely divisible by number B and if so then how many\n",
        "times it can be divisible."
      ],
      "metadata": {
        "id": "D1QmTfuSTNCb"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "a= int(input())\n",
        "b= int(input())\n",
        "c=0\n",
        "d=a\n",
        "\n",
        "while a%b==0:\n",
        "  a= a/b\n",
        "  c=c+1\n",
        "if c>0:\n",
        "  print(f'{d} is divisible by {b} {c}times')\n",
        "\n",
        "else:\n",
        "  print(f'{d} is not purly divisible by {b}, there will be a remainder {d%b}')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "eKzZJ6vJTOVC",
        "outputId": "d4427ef0-6963-460c-cc26-17563cae52ed"
      },
      "execution_count": 32,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1000\n",
            "13\n",
            "1000 is not purly divisible by 13, there will be a remainder 12\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Q6. Create a list containing 25 int type data. Using for loop and if-else condition print if the element is\n",
        "divisible by 3 or not."
      ],
      "metadata": {
        "id": "1QfrPIaRXPV6"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "l= list(range(17,66,2))"
      ],
      "metadata": {
        "id": "maZrziiwXgqy"
      },
      "execution_count": 60,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "len(l)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "PRJLNGl7XoEx",
        "outputId": "6a881b5e-7cd6-4b2c-91ea-1200463ce6b1"
      },
      "execution_count": 61,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "25"
            ]
          },
          "metadata": {},
          "execution_count": 61
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(l,end='')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "y-Vbyuu7YFrc",
        "outputId": "96cf3425-3b44-40ab-d26f-62b03bf8c80f"
      },
      "execution_count": 62,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65]"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "for i in l:\n",
        "  if i%3==0:\n",
        "    print(f'*****{i} is divisible by 3*****')\n",
        "  else:\n",
        "    print(f'{i} is not divisible by the remainder is {i%3}')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "zmi4Fo30YNK8",
        "outputId": "05ebf260-00d0-4ec5-95a8-4e372be78259"
      },
      "execution_count": 65,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "17 is not divisible by the remainder is 2\n",
            "19 is not divisible by the remainder is 1\n",
            "*****21 is divisible by 3*****\n",
            "23 is not divisible by the remainder is 2\n",
            "25 is not divisible by the remainder is 1\n",
            "*****27 is divisible by 3*****\n",
            "29 is not divisible by the remainder is 2\n",
            "31 is not divisible by the remainder is 1\n",
            "*****33 is divisible by 3*****\n",
            "35 is not divisible by the remainder is 2\n",
            "37 is not divisible by the remainder is 1\n",
            "*****39 is divisible by 3*****\n",
            "41 is not divisible by the remainder is 2\n",
            "43 is not divisible by the remainder is 1\n",
            "*****45 is divisible by 3*****\n",
            "47 is not divisible by the remainder is 2\n",
            "49 is not divisible by the remainder is 1\n",
            "*****51 is divisible by 3*****\n",
            "53 is not divisible by the remainder is 2\n",
            "55 is not divisible by the remainder is 1\n",
            "*****57 is divisible by 3*****\n",
            "59 is not divisible by the remainder is 2\n",
            "61 is not divisible by the remainder is 1\n",
            "*****63 is divisible by 3*****\n",
            "65 is not divisible by the remainder is 2\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Q7. What do you understand about mutable and immutable data types? Give examples for both showing\n",
        "this property."
      ],
      "metadata": {
        "id": "eIsTLkSAZVYS"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "'''type of data which can be modified by the user is mutable data and type of data which can not be changed by the user can be called as unmutable data type.\n",
        "for  example list can be modified we can change its elements so it is mutable while a string or a tuple data type can not be changed'''"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 53
        },
        "id": "3NPYhamQZXQK",
        "outputId": "7baee5d1-135c-41d3-b5ba-ed1228f67064"
      },
      "execution_count": 66,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'type of data which can be modified by the user is mutable data and type of data which can not be changed by the user can be called as unmutable data type.\\nfor  example list can be modified we can change its elements so it is mutable while a string or a tuple data type can not be changed'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 66
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "a=[1,2,3,4]\n",
        "print(a)\n",
        "a[3]= 10\n",
        "print(a)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "8FhdVQgNaCeq",
        "outputId": "737114f2-bfa7-48eb-fd36-abcf2f7e2080"
      },
      "execution_count": 67,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[1, 2, 3, 4]\n",
            "[1, 2, 3, 10]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "b=(1,2,3,4,6)\n",
        "print(b)\n",
        "b[4]= 15\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 235
        },
        "id": "51ge9cmAaMJy",
        "outputId": "0da88948-b41f-42fa-8565-407986677ec3"
      },
      "execution_count": 68,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "(1, 2, 3, 4, 6)\n"
          ]
        },
        {
          "output_type": "error",
          "ename": "TypeError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-68-4efbffbd9b38>\u001b[0m in \u001b[0;36m<cell line: 3>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0mb\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m2\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m3\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m4\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m6\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      2\u001b[0m \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mb\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 3\u001b[0;31m \u001b[0mb\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m4\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m=\u001b[0m \u001b[0;36m15\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      4\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mTypeError\u001b[0m: 'tuple' object does not support item assignment"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "c= 'string'\n",
        "print(c[3])\n",
        "c[3]='j'"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 217
        },
        "id": "RoerPHDranoR",
        "outputId": "32b1acb4-575b-4bc0-f279-e79915b41e94"
      },
      "execution_count": 69,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "i\n"
          ]
        },
        {
          "output_type": "error",
          "ename": "TypeError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-69-449531f0a05f>\u001b[0m in \u001b[0;36m<cell line: 3>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0mc\u001b[0m\u001b[0;34m=\u001b[0m \u001b[0;34m'string'\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      2\u001b[0m \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mc\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m3\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 3\u001b[0;31m \u001b[0mc\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m3\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m'j'\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;31mTypeError\u001b[0m: 'str' object does not support item assignment"
          ]
        }
      ]
    }
  ]
}