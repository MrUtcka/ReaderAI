from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
import keyboard

def summarize_text(text, compression):
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
            print(summarize_text(text_to_summ, text_to_summ.count('.') // 2 + 1))
        elif(compression_force == '1'):
            print(summarize_text(text_to_summ, 3))
        else:
            print('Неверные данные, повторите еще раз.')
        print('-' * 50)

if __name__ == '__main__':
    main()
