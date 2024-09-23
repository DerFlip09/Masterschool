import string


TEXT = """
T xv xnrixcj dxr wurkf ud Nuwcuw, xwc xa T mxne tw kfi akriika ud
Qikiraborzf, T diin x hunc wurkfirw briiyi qnxj oquw vj hfiiea, mfthf
brxhia vj wirlia xwc dtnna vi mtkf cintzfk. Cu juo owcirakxwc kfta
diintwz? Kfta briiyi, mfthf fxa krxlinnic druv kfi riztuwa kumxrca
mfthf T xv xclxwhtwz, ztlia vi x durikxaki ud kfuai thj hntvia.
Twaqtrtkic bj kfta mtwc ud qruvtai, vj cxjcrixva bihuvi vuri dirliwk
xwc ltltc. T krj tw lxtw ku bi qiraoxcic kfxk kfi quni ta kfi aixk ud
druak xwc ciaunxktuw; tk ilir qriaiwka tkaind ku vj tvxztwxktuw xa kfi
riztuw ud bixokj xwc cintzfk. Kfiri, Vxrzxrik, kfi aow ta dur ilir
ltatbni, tka bruxc ctae soak aetrktwz kfi furtyuw xwc ctddoatwz x
qirqikoxn aqniwcuor. Kfiri—dur mtkf juor nixli, vj atakir, T mtnn qok
auvi kroak tw qrihictwz wxltzxkura—kfiri awum xwc druak xri bxwtafic;
xwc, axtntwz ulir x hxnv aix, mi vxj bi mxdkic ku x nxwc aorqxaatwz tw
muwcira xwc tw bixokj ilirj riztuw ftkfirku ctahuliric uw kfi fxbtkxbni
znubi. Tka qrucohktuwa xwc dixkoria vxj bi mtkfuok igxvqni, xa kfi
qfiwuviwx ud kfi fixliwnj buctia owcuobkicnj xri tw kfuai owctahuliric
auntkocia. Mfxk vxj wuk bi igqihkic tw x huowkrj ud ikirwxn ntzfk? T
vxj kfiri ctahulir kfi muwcruoa qumir mfthf xkkr"""


def get_top_n_freq_chars():
    char_with_appearances = {}
    for char in TEXT:
        char = char.lower()
        if char not in char_with_appearances and char in string.ascii_letters:
            char_with_appearances[char] = 1
        elif char in string.ascii_letters:
            char_with_appearances[char] += 1
    return char_with_appearances


def value_getter(item):
    return item[1]


def top_n_char(freq, n):
    sorted_list_of_appearances = sorted(freq.items(), key=value_getter, reverse=True)  # sorts
    for i in range(n):
        char, appearance = sorted_list_of_appearances[i]
        print(f"{char}: {appearance}")


a = TEXT.replace("i", "e")
b = a.replace("I", "e")
c = b.replace("t", "i")
d = c.replace("T", "i")
e = d.replace("k", "t")
f = e.replace("K", "t")
g = f.replace("r", "o")
h = g.replace("R", "o")
print(h)

