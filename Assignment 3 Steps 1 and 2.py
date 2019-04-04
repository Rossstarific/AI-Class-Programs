import nltk
from urllib import request
from nltk import Tree
from nltk.draw.tree import TreeView
import os
from nltk.tag import pos_tag
from nltk.tokenize import RegexpTokenizer
import re
from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import PunktSentenceTokenizer
import string
import matplotlib.pyplot as plt
from nltk.corpus import reuters
from collections import Counter

'''baseurl = "http://www.gutenberg.org/files/1787/1787.txt"
baseresponse = request.urlopen(baseurl)
baseraw = baseresponse.read().decode('utf8')'''

Cfile = open("ComedyWords.txt","w")
Tfile = open("TragedyWords.txt","w")
ToBefile = open("ToBeOrNotToBe.txt","r")
Dumbledorefile = open("Dumbledore.txt","r")

names = ['theseus', 'egeus', 'lysander', 'demetreus', 'philostrate', 'quince', 'snug', 'bottom', 'flute',
        'snout', 'starveling','hippolyta', 'hermia', 'helena', 'oberon', 'titania', 'puck', 'peaseblossom',
        'cobweb','moth','mustardseed','pyramus','thisby','wall','moonshine','lion','duke', 'venice','prince',
        'morocco','arragon','antonio','bassanio','solanio','salerio','gratiano','lorenzo','shylock','tubal',
        'launcelot','gobbo','leonardo','balthasar','stephano','sirra','portia','nerissa','jessica','magnificoes',
        'gaoler','robin','goodfellow','solinus','aegeon','antipholus','syracuse','dromio','ephesus','balthazar',
        'angelo','merchant','pinch','aemilia','adriana','luciana','luce','courtezan','officer','hymen','hippolita',
        'emelia','nymphs','nymph','queen','knight','palamon','arcite','valerius','perithous','herald','gentleman',
        'messenger','wooer','keeper','jaylor','doctor','countreyman','countreymen','taborer','gerrold','frederick',
        'amiens','jaques','le','beau','charles','orlando','adam','dennis','touchstone','oliver','s','olivers','martext',
        'corin','silvius','william','hymen','rosalind','celia','phebe','audrey','forester','act','scene','enter','exit',
        'exeunt','i','ii','iii','iv','v','electronic', 'version', 'complete', 'work', 'shakespeare', 'copyright',
        'world', 'library', 'inc', 'provided', 'project', 'gutenberg', 'etext', 'carnegie', 'mellon', 'university',
        'permission', 'electronic', 'machine', 'readable', 'copy', 'may', 'distributed', 'long', 'copy', 'others',
        'personal', 'use', 'distributed', 'used', 'commercially', 'prohibited', 'commercial', 'distribution',
        'includes', 'service', 'charge', 'download', 'membership','othello','desdemona','iago','emilia','cassio',
        'brabantio','gratiano','lodovico','roderigo','bianca','montano','clown','senator','senators','sailor','sailors'
        'escalus','paris','montague','capulet','romeo','mercutio','benvolio','tybalt','friar','lawrence','john','balthasar',
        'sampson','gregory','peter','abraham','apothecary','musician','musicians','chorus','page','juliet','nurse',
        'julius','caesar','octavius','mark','antony','lepidus','marcus','brutus','cassius','casca','trebonius','caius',
        'ligarius','decius','brutus','metellus','cimber','cinna','calpurnia','portia','cicero','popilius','lena','flavius',
        'marullus','tribune','cato','lucilius','titinius','messala','volumnius','artemidorus','cinna','varro','clitus',
        'claudio','strato','lucius','dardanius','pindarius','ghost','soothsayer','poet','claudius','marcellus','hamlet',
        'polonius','chamberlain','voltemand','cornelius','rosencrantz','guildenstern','osric','priest','bernardo','francisco',
        'reynaldo','player','players','fortinbras','norway','gertrude','ophelia','ber','fran','hor','mar','elsinore','king',
        'cor','laer','pol','ham','oph','rey','ros','guil','volt','lear','burgundy','cornwall','albany','kent','gloucester','glou',
        'alb','edgar','edmund','curan','fool','oswald','goneril','gon','regan','cordelia','edm','reg','cor','bur','france',
        'edg','osw','ti','th','u']
 
def allComedies():
    def As_You_Like_It():
        url = "http://www.gutenberg.org/files/1786/1786.txt"
        response = request.urlopen(url)
        raw = response.read().decode('utf8')
        raw = raw[10672:149648]
        raw = raw.translate(str.maketrans('','',string.punctuation))
        raw = raw.translate(str.maketrans('','',string.digits))
        raw.replace('\n', ' ')
        return raw;

    def Two_Noble_Kinsman():
        url = "http://www.gutenberg.org/files/1542/1542.txt"
        response = request.urlopen(url)
        raw = response.read().decode('utf8')
        raw = raw[13394:160639]
        raw = raw.translate(str.maketrans('','',string.punctuation))
        raw = raw.translate(str.maketrans('','',string.digits))
        raw.replace('\n', ' ')
        return raw;

    def Comedy_Of_Errors():
        url = "http://www.gutenberg.org/files/1104/1104.txt"
        response = request.urlopen(url)
        raw = response.read().decode('utf8')
        raw = raw[11006:104661]
        raw = raw.translate(str.maketrans('','',string.punctuation))
        raw = raw.translate(str.maketrans('','',string.digits))
        raw.replace('\n', ' ')
        return raw;

    def Merchant_Of_Venice():
        url = "http://www.gutenberg.org/files/1779/1779.txt"
        response = request.urlopen(url)
        raw = response.read().decode('utf8')
        raw = raw[10889:144834]
        raw = raw.translate(str.maketrans('','',string.punctuation))
        raw = raw.translate(str.maketrans('','',string.digits))
        raw.replace('\n', ' ')
        return raw;

    def A_Midsummer_Nights_Dream():
        url = "http://www.gutenberg.org/files/1778/1778.txt"
        response = request.urlopen(url)
        raw = response.read().decode('utf8')
        raw = raw[10755:120599]
        raw = raw.translate(str.maketrans('','',string.punctuation))
        raw = raw.translate(str.maketrans('','',string.digits))
        raw.replace('\n', ' ')
        return raw;

    return As_You_Like_It() + ' ' + Two_Noble_Kinsman() + ' ' + Comedy_Of_Errors() + ' ' + Merchant_Of_Venice() + ' ' + A_Midsummer_Nights_Dream();


def allTragedies():
    def Othello():
        url = "http://www.gutenberg.org/files/1793/1793.txt"
        response = request.urlopen(url)
        raw = response.read().decode('utf8')
        raw = raw[10510:187992]
        raw = raw.translate(str.maketrans('','',string.punctuation))
        raw = raw.translate(str.maketrans('','',string.digits))
        raw.replace('\n', ' ')
        return raw;

    def Romeo_And_Juliet():
        url = "http://www.gutenberg.org/files/1513/1513.txt"
        response = request.urlopen(url)
        raw = response.read().decode('utf8')
        raw = raw[13961:159212]
        raw = raw.translate(str.maketrans('','',string.punctuation))
        raw = raw.translate(str.maketrans('','',string.digits))
        raw.replace('\n', ' ')
        return raw;

    def Julius_Caesar():
        url = "http://www.gutenberg.org/files/1785/1785.txt"
        response = request.urlopen(url)
        raw = response.read().decode('utf8')
        raw = raw[11252:140870]
        raw = raw.translate(str.maketrans('','',string.punctuation))
        raw = raw.translate(str.maketrans('','',string.digits))
        raw.replace('\n', ' ')
        return raw;

    def Hamlet():
        url = "http://www.gutenberg.org/files/1787/1787.txt"
        response = request.urlopen(url)
        raw = response.read().decode('utf8')
        raw = raw[10785:210063]
        raw = raw.translate(str.maketrans('','',string.punctuation))
        raw = raw.translate(str.maketrans('','',string.digits))
        raw.replace('\n', ' ')
        return raw;

    def King_Lear():
        url = "http://www.gutenberg.org/files/1794/1794.txt"
        response = request.urlopen(url)
        raw = response.read().decode('utf8')
        raw = raw[10549:185333]
        raw = raw.translate(str.maketrans('','',string.punctuation))
        raw = raw.translate(str.maketrans('','',string.digits))
        raw.replace('\n', ' ')
        return raw;

    return Othello() + ' ' + Romeo_And_Juliet() + ' ' + Julius_Caesar() + ' ' + Hamlet() + ' ' + King_Lear()


def finalizePlays(allPlays):
    wordnet = nltk.WordNetLemmatizer()
    stop = nltk.corpus.stopwords.words('english')
    allPlays = [i for i in word_tokenize(allPlays.lower()) if i not in stop]
    allPlays = ' '.join(allPlays)
    tagPlays = pos_tag(allPlays.split())
    playWords = [word for word,tag in tagPlays if tag != "NNP" and tag !="NNPS"] 
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(allPlays)
    update_tokens = []
    for i in range(len(tokens)):
        if tokens[i] in names:
            pass
        else:
            update_tokens.append(tokens[i])
    for i in range(len(update_tokens)):
        update_tokens[i] = wordnet.lemmatize(update_tokens[i])
    
    return update_tokens


def CMost50():
    fdist = FreqDist(finalizePlays(allComedies()))
    return fdist.most_common(50);
def TMost50():    
    fdist = FreqDist(finalizePlays(allTragedies()))
    return fdist.most_common(50);

Cfile.write(str(CMost50()))
Cfile.close()

Tfile.write(str(TMost50()))
Tfile.close()

def getToBe():
    speech = ToBefile.read()#.replace('\n',' ')
    return speech;

def getDumbledore():
    speech = Dumbledorefile.read()#.replace('\n',' ')
    return speech;

def getDumbleFirstThree():
    sentences = getDumbledore()
    sentences = sentences[0:288]
    return sentences;

def getToBeFirstThree():
    sentences = getToBe()
    sentences = sentences[0:375]
    return sentences;

def speechTrees(text):
    sample_text = text
    custTokenizer = PunktSentenceTokenizer(text)
    tokenized = custTokenizer.tokenize(sample_text)
    try:
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            chunkGram = """
                        S: {<NP><VP>} 
                        NP: {<DT>?<JJ>*<NN>}
                            {<DT>?<JJ>*<PRP>}
                            {<DT>?<JJ>*<NNP>}
                            {<DT>?<JJ>*<NNS>}
                        PP: {<P><NP>}
                        VP: {<VB><NP>|<VP><PP>}
                        IF: {<TO><VB>}
                        P: {<IN><NP>}
                        """
            chunkParser = nltk.RegexpParser(chunkGram)
            chunked = chunkParser.parse(tagged)
            tree = TreeView(chunked)
    except Exception as e:
        print(str(e))

'''def speechParseTree(text):
    tree = Tree.fromstring()'''
#speechTrees(getDumbleFirstThree())
#speechTrees(getToBeFirstThree())
#speechTrees("There is much that I would like to say to you all tonight, but I must first acknowledge the loss of a very fine person who should be sitting here, enjoying our feast with us.")
#speechTrees("I would like you all, please, to stand and raise your glasses to Cedric Diggory.")   





