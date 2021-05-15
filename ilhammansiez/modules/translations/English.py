RUN_STRINGS = (
    "Menurutmu kemana kamu akan pergi?",
    "Hah? Apa? Apakah mereka lolos?",
    "ZZzzZZzz ... Hah? Apa? Oh, hanya mereka lagi, lupakan.",
    "Kembali kesini!",
    "Tidak terlalu cepat ...",
    "Awas ke dinding!",
    "Jangan tinggalkan aku sendiri dengan mereka !!",
    "Kamu lari, kamu mati.",
    "Bercanda, aku ada dimana-mana",
    "Kamu akan menyesali itu ...",
    "Kamu juga bisa mencoba /kickme, kudengar itu menyenangkan.",
    "Ganggu orang lain, tidak ada yang peduli.",
    "Kamu bisa lari, tapi kamu tidak bisa bersembunyi.",
    "Apakah hanya itu yang kamu punya?",
    "Saya di belakang Anda...",
    "Anda punya teman!",
    "Kita bisa melakukan ini dengan cara mudah, atau cara sulit.",
    "Anda tidak mengerti, bukan?",
    "Ya, sebaiknya kau lari!",
    "Tolong, ingatkan saya betapa saya peduli?",
    "Aku akan berlari lebih cepat jika jadi kamu.",
    "Itu pasti droid yang kami cari.",
    "Semoga peluang selalu menguntungkan Anda.",
    "Kata-kata terakhir yang terkenal.",
    "Dan mereka menghilang selamanya, tidak pernah terlihat lagi.",
    "\" Oh, lihat aku! Saya sangat keren, saya bisa lari dari bot! \ "- orang ini",
    "Ya ya, cukup ketuk /kickme.",
    "Ini, ambil cincin ini dan pergilah ke Mordor saat kamu melakukannya.",
    "Legenda mengatakan, mereka masih berjalan ...",
    "Tidak seperti Harry Potter, orang tuamu tidak bisa melindungimu dariku.",
    "Ketakutan menyebabkan kemarahan. Kemarahan mengarah pada kebencian. Kebencian menyebabkan penderitaan. Jika Anda terus berlari dalam ketakutan, Anda mungkin"
    "jadilah Vader berikutnya.",
    "Beberapa kalkulasi nanti, saya telah memutuskan minat saya pada kejahatan Anda tepat 0.",
    "Legenda mengatakan, mereka masih berjalan.",
    "Teruskan, kami tidak yakin kami menginginkanmu di sini.",
    "Kamu seorang penyihir- Oh. Tunggu. Kamu bukan Harry, teruslah bergerak.",
    "TIDAK BERLARI DI HALLWAYS!",
    "Hasta la vista, sayang.",
    "Siapa yang membiarkan anjing keluar?",
    "Ini lucu, karena tidak ada yang peduli.",
    "Ah, sayang sekali. Aku suka yang itu.",
    "Terus terang, sayangku, aku tidak peduli.",
    "Milkshake saya membawa semua anak laki-laki ke halaman ... Jadi lari lebih cepat!",
    "Anda tidak bisa MENANGANI kebenaran!",
    "Dahulu kala, di galaksi yang sangat jauh ... Seseorang akan peduli tentang itu. Tapi sekarang tidak lagi.",
    "Hei, lihat mereka! Mereka lari dari palu yang tak terelakkan ... Manis.",
    "Han menembak lebih dulu. Aku juga.",
    "Apa yang kamu kejar, kelinci putih?",
    "Seperti yang dikatakan The Doctor ... LARI!",
)

SLAP_TEMPLATES = (
    "{user1} {hits} {user2} with a {item}.",
    "{user1} {hits} {user2} in the face with a {item}.",
    "{user1} {hits} {user2} around a bit with a {item}.",
    "{user1} {throws} a {item} at {user2}.",
    "{user1} grabs a {item} and {throws} it at {user2}'s face.",
    "{user1} launches a {item} in {user2}'s general direction.",
    "{user1} starts slapping {user2} silly with a {item}.",
    "{user1} pins {user2} down and repeatedly {hits} them with a {item}.",
    "{user1} grabs up a {item} and {hits} {user2} with it.",
    "{user1} ties {user2} to a chair and {throws} a {item} at them.",
    "{user1} gave a friendly push to help {user2} learn to swim in lava."
)

ITEMS = (
    "wajan besi cor",
    "trout besar",
    "tongkat pemukul baseball",
    "tongkat kriket",
    "tongkat kayu",
    "kuku",
    "pencetak",
    "sekop",
    "Monitor CRT",
    "buku teks fisika",
    "pemanggang roti",
    "potret Richard Stallman",
    "televisi",
    "truk lima ton",
    "gulungan lakban",
    "Book",
    "laptop",
    "televisi tua",
    "karung batu",
    "ikan trout pelangi",
    "ayam karet",
    "kelelawar berduri",
    "alat pemadam Api",
    "batu berat",
    "bongkahan kotoran",
    "sarang lebah",
    "sepotong daging busuk",
    "beruang",
    "banyak batu bata",
)

THROW = (
    "throws",
    "flings",
    "chucks",
    "hurls",
)

HIT = (
    "hits",
    "whacks",
    "slaps",
    "smacks",
    "bashes",
)

MARKDOWN_HELP = """
Markdown is a very powerful formatting tool supported by telegram. {} has some enhancements, to make sure that \
saved messages are correctly parsed, and to allow you to create buttons.

- <code>_italic_</code>: wrapping text with '_' will produce italic text
- <code>*bold*</code>: wrapping text with '*' will produce bold text
- <code>`code`</code>: wrapping text with '`' will produce monospaced text, also known as 'code'
- <code>[sometext](someURL)</code>: this will create a link - the message will just show <code>sometext</code>, \
and tapping on it will open the page at <code>someURL</code>.
EG: <code>[test](example.com)</code>

- <code>[buttontext](buttonurl:someURL)</code>: this is a special enhancement to allow users to have telegram \
buttons in their markdown. <code>buttontext</code> will be what is displayed on the button, and <code>someurl</code> \
will be the url which is opened.
EG: <code>[This is a button](buttonurl:example.com)</code>

If you want multiple buttons on the same line, use :same, as such:
<code>[one](buttonurl://example.com)
[two](buttonurl://google.com:same)</code>
This will create two buttons on a single line, instead of one button per line.
"""

EnglishStrings = {
    "send-help": """*Main commands available*:
 - /start: start the bot
 - /help or /help <module name>: PM's you info about that module.
 - /lang: Change bot language
 - /settings:
   - in PM: will send you your settings for all supported modules.
   - in a group: will redirect you to pm, with all that chat's settings.
   {}
   """,

    "send-group-settings": """Hi there! There are quite a few settings for *{}* - go ahead and pick what
you're interested in.""",

#Misc
"RUNS-K": RUN_STRINGS,
"SLAP_TEMPLATES-K": SLAP_TEMPLATES,
"ITEMS-K": ITEMS,
"HIT-K": HIT,
"THROW-K": THROW,
"ITEMP-K": ITEMS,
"ITEMR-K": ITEMS,
"MARKDOWN_HELP-K": MARKDOWN_HELP,

#GDPR
"send-gdpr": """Your personal data has been deleted.\n\nNote that this will not unban \
you from any chats, as that is telegram data, not YanaBot data.
Flooding, warns, and gbans are also preserved, as of \
[this](https://ico.org.uk/for-organisations/guide-to-the-general-data-protection-regulation-gdpr/individual-rights/right-to-erasure/), "
which clearly states that the right to erasure does not apply \
\"for the performance of a task carried out in the public interest\", as is \
the case for the aforementioned pieces of data."""

}
