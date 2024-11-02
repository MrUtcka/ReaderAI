import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer

def summarize_text_nltk(text, compression):
    stopWords = set(stopwords.words("english"))
    words = word_tokenize(text)

    freqTable = dict()
    for word in words:
        word = word.lower()
        if word in stopWords:
            continue
        if word in freqTable:
            freqTable[word] += 1
        else:
            freqTable[word] = 1

    sentences = sent_tokenize(text)
    sentenceValue = dict()

    for sentence in sentences:
        for word, freq in freqTable.items():
            if word in sentence.lower():
                if word in sentence.lower():
                    if sentence in sentenceValue:
                        sentenceValue[sentence] += freq
                    else:
                        sentenceValue[sentence] = freq

                        sumValues = 0

    for sentence in sentenceValue:
        sumValues += sentenceValue[sentence]

    average = int(sumValues / len(sentenceValue))
    summary = ''

    for sentence in sentences:
        if (sentence in sentenceValue) and (sentenceValue[sentence] > (compression * average)):
            summary += ' ' + sentence

    return summary


def summarize_text_sumy(text, compression):
    parser = PlaintextParser.from_string(text, Tokenizer("russian"))
    summarizer_lex = LexRankSummarizer()

    summary = summarizer_lex(parser.document, compression)
    lex_summary = ""
    for sentence in summary:
        lex_summary += str(sentence)

    return lex_summary


def main():
    print('------| Сжиматель текста |------')

    while True:
        text_to_summ = input('Введите текст для сжатия: ')
        compression_force = input('Введите силу сжатия(0 - Слабое, 1 - Сильное): ')

        print('-' * 50)

        if(compression_force == '0'):
            summ = summarize_text_nltk(text_to_summ, 1.2)
            if(len(summ) == 0):
                print(summarize_text_sumy(text_to_summ, text_to_summ.count('.') // 2 + 1))
            else:
                print(summ)
        elif(compression_force == '1'):
            summ = summarize_text_nltk(text_to_summ, 1.6)
            if(len(summ) == 0):
                print(summarize_text_sumy(text_to_summ, 3))
            else:
                print(summ)
        else:
            print('Неверные данные, повторите еще раз.')

        print('-' * 50)


if __name__ == '__main__':
    main()
