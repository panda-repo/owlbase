import os

api_id = int(os.environ.get("API_ID", "27867060"))
api_hash = os.environ.get("API_HASH", "4925060cfe1908846070a018e5f5da02")
bot_token = os.environ.get("BOT_TOKEN", "5980751640:AAGOYsE85FHjgr56Rk2GlemxXyN_K0eb4OU")
# =========================================================== #

db_url = os.environ.get("DB_URL", "mongodb+srv://owl:<password>@owlbase.20i0fnf.mongodb.net/?retryWrites=true&w=majority")
db_name = os.environ.get("DB_NAME", "menfess")
# =========================================================== #

channel_1 = int(os.environ.get("CHANNEL_1", "-1001162542681"))
channel_2 = int(os.environ.get("CHANNEL_2", "-1001884106616"))
channel_log = int(os.environ.get("CHANNEL_LOG", "-1001883858306"))
# =========================================================== #

id_admin = int(os.environ.get("ID_ADMIN", "5633222043"))
# =========================================================== #

batas_kirim = int(os.environ.get("BATAS_KIRIM", "5"))
batas_talent = int(os.environ.get("BATAS_TALENT", "10"))
batas_daddy_sugar = int(os.environ.get("BATAS_DADDY_SUGAR", "10"))
batas_moansgirl = int(os.environ.get("BATAS_MOANSGIRL", "10"))
batas_moansboy = int(os.environ.get("BATAS_MOANSBOY", "10"))
batas_gfrent = int(os.environ.get("BATAS_GFRENT", "10"))
batas_bfrent = int(os.environ.get("BATAS_BFRENT", "10"))
# =========================================================== #

biaya_kirim = int(os.environ.get("BIAYA_KIRIM", "10"))
biaya_talent = int(os.environ.get("BIAYA_TALENT", "80"))
biaya_daddy_sugar = int(os.environ.get("BIAYA_DADDY_SUGAR", "70"))
biaya_moansgirl = int(os.environ.get("BIAYA_MOANSGIRL", "60"))
biaya_moansboy = int(os.environ.get("BIAYA_MOANSBOY", "50"))
biaya_gfrent = int(os.environ.get("BIAYA_GFRENT", "40"))
biaya_bfrent = int(os.environ.get("BIAYA_BFRENT", "30"))
# =========================================================== #

hastag = os.environ.get("HASTAG", "#NekoGirl #NekoBoy #NekoAsk #NekoFind #NekoSpill #NekoStory #NekoTalent").replace(" ", "|").lower()
# =========================================================== #

pic_boy = os.environ.get("PIC_BOY", "https://telegra.ph/file/387bdabb03deaf94fa4e9.jpg")
pic_girl = os.environ.get("PIC_GIRL", "https://telegra.ph/file/2bc2dc1fad8e33cf69e6d.jpg")
pic_talentgirl = os.environ.get("PIC_TALENTGIRL", "https://telegra.ph/file/95801451d752f089f8e1e.jpg")
pic_daddysugar = os.environ.get("PIC_DADDYSUGAR", "https://telegra.ph/file/14ca710511333621be61d.jpg")
pic_moansgirl = os.environ.get("PIC_MOANSGIRL" , "https://telegra.ph/file/10232ac2404b3e822f99d.jpg")
pic_moansboy = os.environ.get("PIC_MOANSBOY" , "https://telegra.ph/file/90359cf42550732058d20.jpg")
pic_gfrent = os.environ.get("PIC_GFRENT" , "https://telegra.ph/file/432e8cb26179ade6eba70.jpg")
pic_bfrent = os.environ.get("PIC_BFRENT" , "https://telegra.ph/file/e0dc732430d9b1b0cbfa1.jpg")
pic_owner = os.environ.get("PIC_OWNER" , "https://telegra.ph/file/52a68a944487567d30826.jpg")
pic_neko = os.environ.get("PIC_NEKO" , "https://telegra.ph/file/2d46007dd7d22645c4ec3.jpg")
pic_admin = os.environ.get("PIC_ADMIN" , "https://telegra.ph/file/30c7b36f68d69840a762c.jpg")


# =========================================================== #

pesan_join = os.environ.get("PESAN_JOIN", "Tidak dapat diakses harap join terlebih dahulu")
start_msg = os.environ.get("START_MSG", """"
{mention},Silahkan gunakan hastag:

#NekoBoy / #NekoGirl untuk Mencari Pasangan,Teman , Partner dll
#NekoAsk untuk Bertanya
#NekoStory untuk Berbagi Cerita
#NekoSpill untuk Spill Masalah
#NekoFind untuk Mencari Pasangan, Teman, Partner dll

{fullname} 🌱\n\nIni adalah bot menfess, semua pesan yang kamu kirim akan masuk ke channel secara anonymous. ketik /help""")

gagalkirim_msg = os.environ.get("GAGAL_KIRIM", """
{mention}, pesan mu gagal terkirim silahkan gunakan hastag:

#NekoBoy / #NekoGirl untuk Mencari Pasangan, Teman , Partner dll
#NekoAsk untuk Bertanya
#NekoStory untuk Berbagi Cerita
#NekoSpill untuk Spill Masalah
#NekoFind untuk Mencari Pasangan, Teman, Partner dll
""")
