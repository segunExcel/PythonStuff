{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNXE0ZsyHMQq7OvMWFvLcRj",
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
        "<a href=\"https://colab.research.google.com/github/segunExcel/PythonStuff/blob/main/ass1.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Load File into 2D list"
      ],
      "metadata": {
        "id": "4xWMmeqTFjJX"
      }
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "Uau7UHPalYp-"
      },
      "outputs": [],
      "source": [
        "def load_data_from_file_into_2D_list(filename: str) -> list:\n",
        "\n",
        "  data_table = []\n",
        "  sublist = []\n",
        "\n",
        "  with open(filename) as file:\n",
        "    file_contents = file.readlines()\n",
        "\n",
        "  for line in file_contents:\n",
        "    if line.startswith('END'):\n",
        "      if len(sublist) > 0:\n",
        "        data_table.append(sublist)\n",
        "      break\n",
        "\n",
        "    elif line.startswith('COLUMN'):\n",
        "      column_name = ' '.join(line.strip().split(' ')[1:])\n",
        "\n",
        "      if len(sublist) > 0:\n",
        "        data_table.append(sublist)\n",
        "      sublist = [column_name]\n",
        "\n",
        "    else:\n",
        "      sublist.append(line.strip())\n",
        "  return data_table"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Load File into Dict"
      ],
      "metadata": {
        "id": "u1_Oc8hRFo84"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def load_data_from_file_into_dictionary(filename: str) -> dict:\n",
        "  data_table = {}\n",
        "  data = []\n",
        "  column_name=''\n",
        "  with open(filename) as file:\n",
        "    for line in file:\n",
        "      if line.startswith(\"COLUMN\"):\n",
        "        if len(data) > 0:\n",
        "          data_table[column_name] = data\n",
        "          data = []\n",
        "        column_name = ' '.join(line.split(' ')[1:]).strip()\n",
        "      elif line [:3] == \"END\":\n",
        "        if len(data) > 0:\n",
        "          data_table[column_name] = data\n",
        "          break\n",
        "      else:\n",
        "        data.append(line.strip())\n",
        "  return data_table"
      ],
      "metadata": {
        "id": "lTNQUeJ9Fs1A"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Return Sublist from either dict or list"
      ],
      "metadata": {
        "id": "5x5JmRCihpGV"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def return_sublist_from_either_dictionary_or_2D_list(data_table:list |dict, key:str)-> list:\n",
        "    if isinstance(data_table, dict): # check if the data_table is a dictionary\n",
        "        return data_table[key]\n",
        "    elif isinstance(data_table, list): # check if the data_table is a 2D list\n",
        "        for row in data_table: # iterate through the rows of the 2D list\n",
        "            if row[0] == key: # check if the first element of the row is equal to the key\n",
        "                sublist =[]\n",
        "                for element in row[1:]: # iterate through the rest of the row after the first element\n",
        "                    sublist.append(element)\n",
        "                return sublist\n",
        "    else:\n",
        "        raise ValueError(\"data_table must be a dictionary or a 2D list\")"
      ],
      "metadata": {
        "id": "bmWQ4ofqmRN7"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Sublist Total"
      ],
      "metadata": {
        "id": "LOa1038TBls4"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def return_sublist_total_from_either_dictionary_or_2D_list(data_table: list | dict, key: str) -> float | None:\n",
        "    sublist = return_sublist_from_either_dictionary_or_2D_list(data_table, key)\n",
        "    if sublist is None:  # If key not found\n",
        "        return None\n",
        "\n",
        "    sublist_total = 0\n",
        "    for item in sublist:\n",
        "        try:\n",
        "            sublist_total += float(item)  # Convert to float and add\n",
        "        except ValueError:\n",
        "            return None  # Return None if any value can't be converted to a number\n",
        "\n",
        "    return sublist_total"
      ],
      "metadata": {
        "id": "sqIwVavY5bzy"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Sublist Mean"
      ],
      "metadata": {
        "id": "QE0tzsaYBsH9"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def return_sublist_mean_from_either_dictionary_or_2D_list(data_table: list | dict, key: str) -> float | None:\n",
        "    sublist = return_sublist_from_either_dictionary_or_2D_list(data_table, key)\n",
        "    if sublist is None or len(sublist) == 0:  # If key not found or sublist is empty\n",
        "        return None\n",
        "\n",
        "    total = 0\n",
        "    count = 0\n",
        "    for item in sublist:\n",
        "        try:\n",
        "            total += float(item)\n",
        "            count += 1\n",
        "        except ValueError:\n",
        "            return None  # Return None if any value can't be converted to a number\n",
        "\n",
        "        sublist_mean = total / count\n",
        "\n",
        "    return sublist_mean  # Calculate mean\n"
      ],
      "metadata": {
        "id": "zO2hoTZsBwIe"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Sublist Median"
      ],
      "metadata": {
        "id": "-EnIpDsIDKK6"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def return_sublist_median_from_either_dictionary_or_2D_list(data_table: list | dict, key: str) -> float | None:\n",
        "    sublist = return_sublist_from_either_dictionary_or_2D_list(data_table, key)\n",
        "    if sublist is None or len(sublist) == 0:  # If key not found or sublist is empty\n",
        "        return None\n",
        "\n",
        "    try:\n",
        "        numeric_values = sorted(float(item) for item in sublist)  # Convert to float and sort\n",
        "    except ValueError:\n",
        "        return None  # Return None if any value can't be converted to a number\n",
        "\n",
        "    length = len(numeric_values)\n",
        "    mid = length // 2\n",
        "\n",
        "    if length % 2 == 1:  # Odd number of elements\n",
        "        return numeric_values[mid]\n",
        "    else:  # Even number of elements\n",
        "        return (numeric_values[mid - 1] + numeric_values[mid]) / 2\n"
      ],
      "metadata": {
        "id": "zwkActgjDMwX"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Total Value From Dictionary or list"
      ],
      "metadata": {
        "id": "5DvuuUP5ExXC"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def return_total_value_from_either_dictionary_or_2D_list(data_table: list | dict) -> float | None:\n",
        "    total = 0\n",
        "    if isinstance(data_table, dict):\n",
        "        for key in data_table:\n",
        "            total = return_sublist_total_from_either_dictionary_or_2D_list(data_table, key)\n",
        "            if total is None:\n",
        "                return None  # If any sublist can't be processed\n",
        "            total += total\n",
        "    elif isinstance(data_table, list):\n",
        "        for sublist in data_table:\n",
        "            if len(sublist) > 0:\n",
        "                key = sublist[0]\n",
        "                sublist_total = return_sublist_total_from_either_dictionary_or_2D_list(data_table, key)\n",
        "                if sublist_total is None:\n",
        "                    return None\n",
        "                total += sublist_total\n",
        "    else:\n",
        "        return None  # Invalid data structure\n",
        "\n",
        "    return total"
      ],
      "metadata": {
        "id": "toEttiJ6FJjg"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "tests"
      ],
      "metadata": {
        "id": "7vMv4sbY9ZQg"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def test_load_data_from_file_into_2D_list():\n",
        "    filename = \"test.txt\"\n",
        "    result = load_data_from_file_into_2D_list(filename)\n",
        "    print(\"2D List Result:\")\n",
        "    print(result)\n",
        "\n",
        "test_load_data_from_file_into_2D_list()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "8wVrIDhP9Zuo",
        "outputId": "433e392e-8a7a-4d55-a10f-4c10ef9bba2e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "2D List Result:\n",
            "[['Products', 'Apples', 'Oranges', 'Bananas'], ['Prices', '1.2', '0.8', '1.5'], ['Quantities', '10', '15', '20']]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def test_load_data_from_file_into_dictionary():\n",
        "    filename = \"test.txt\"\n",
        "    result = load_data_from_file_into_dictionary(filename)\n",
        "    print(\"Dictionary Result:\")\n",
        "    print(result)\n",
        "\n",
        "test_load_data_from_file_into_dictionary()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "dAXJgKLBH73e",
        "outputId": "2a466f81-636e-4e09-cdff-56a6033fed5a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Dictionary Result:\n",
            "{'Products': ['Apples', 'Oranges', 'Bananas'], 'Prices': ['1.2', '0.8', '1.5'], 'Quantities': ['10', '15', '20']}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def test_return_sublist_from_either_dictionary_or_2D_list():\n",
        "    data_dict = {'Products': ['Apples', 'Oranges', 'Bananas'], 'Prices': ['1.2', '0.8', '1.5']}\n",
        "    data_list = [['Products', 'Apples', 'Oranges', 'Bananas'], ['Prices', '1.2', '0.8', '1.5']]\n",
        "\n",
        "    print(\"Sublist from Dictionary (Prices):\", return_sublist_from_either_dictionary_or_2D_list(data_dict, 'Prices'))\n",
        "    print(\"Sublist from 2D List (Prices):\", return_sublist_from_either_dictionary_or_2D_list(data_list, 'Prices'))\n",
        "\n",
        "test_return_sublist_from_either_dictionary_or_2D_list()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "cXUJOTeOIplP",
        "outputId": "f92adb65-f95f-4700-9b66-4af127db1442"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Sublist from Dictionary (Prices): ['1.2', '0.8', '1.5']\n",
            "Sublist from 2D List (Prices): ['1.2', '0.8', '1.5']\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def test_return_sublist_total_from_either_dictionary_or_2D_list():\n",
        "    data_dict = {'Prices': ['1.2', '0.8', '1.5']}\n",
        "    data_list = [['Prices', '1.2', '0.8', '1.5']]\n",
        "\n",
        "    print(\"Total from Dictionary (Prices):\", return_sublist_total_from_either_dictionary_or_2D_list(data_dict, 'Prices'))\n",
        "    print(\"Total from 2D List (Prices):\", return_sublist_total_from_either_dictionary_or_2D_list(data_list, 'Prices'))\n",
        "\n",
        "test_return_sublist_total_from_either_dictionary_or_2D_list()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "zJPniYJJIvn2",
        "outputId": "07220c5c-41db-4747-cfd3-3cbc98f50444"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Total from Dictionary (Prices): 3.5\n",
            "Total from 2D List (Prices): 3.5\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def test_return_sublist_mean_from_either_dictionary_or_2D_list():\n",
        "    data_dict = {'Prices': ['1.2', '0.8', '1.5']}\n",
        "    data_list = [['Prices', '1.2', '0.8', '1.5']]\n",
        "\n",
        "    print(\"Mean from Dictionary (Prices):\", return_sublist_mean_from_either_dictionary_or_2D_list(data_dict, 'Prices'))\n",
        "    print(\"Mean from 2D List (Prices):\", return_sublist_mean_from_either_dictionary_or_2D_list(data_list, 'Prices'))\n",
        "\n",
        "test_return_sublist_mean_from_either_dictionary_or_2D_list()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "hWBrwRXnVhMn",
        "outputId": "a26de59b-0aac-467e-8c4c-700e31cc036f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Mean from Dictionary (Prices): 1.1666666666666667\n",
            "Mean from 2D List (Prices): 1.1666666666666667\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def test_return_total_value_from_either_dictionary_or_2D_list():\n",
        "    data_dict = {\n",
        "        'Prices': ['1.2', '0.8', '1.5'],\n",
        "        'Quantities': ['10', '15', '20']\n",
        "    }\n",
        "    data_list = [\n",
        "        ['Prices', '1.2', '0.8', '1.5'],\n",
        "        ['Quantities', '10', '15', '20']\n",
        "    ]\n",
        "\n",
        "    print(\"Total from Dictionary:\", return_total_value_from_either_dictionary_or_2D_list(data_dict))\n",
        "    print(\"Total from 2D List:\", return_total_value_from_either_dictionary_or_2D_list(data_list))\n",
        "\n",
        "test_return_total_value_from_either_dictionary_or_2D_list()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "-MssFxevcFGo",
        "outputId": "d28eb1d7-4251-4e1b-aebf-1692de871d7e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Total from Dictionary: 48.5\n",
            "Total from 2D List: 48.5\n"
          ]
        }
      ]
    }
  ]
}