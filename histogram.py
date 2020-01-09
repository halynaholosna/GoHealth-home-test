import string

file_path = input(f'Enter text file path ')
file = open(file_path, 'r')
# C:\Users\golos\OneDrive\Рабочий стол\text.docx
text = str(file.read())

# removing punctuation
text1 = text.translate(str.maketrans('', '', string.punctuation))

# converting to the lower case
text2 = text1.lower()

# getting the bigrams and counting them
array = text2.split()

Count = dict()
for i in range(0,len(array)-1):
    bigram=''.join(array[i] +' '+ array[i+1])

    if not bigram in Count:
        Count[bigram] = 1;
    else:
        Count[bigram] = Count[bigram] + 1

print(Count)