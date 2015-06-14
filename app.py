from flask import Flask, render_template, redirect, request

from binascii import hexlify, unhexlify
from markdown2 import markdown

from helpers import get_entries_raw, get_entries, get_entry_mdata, societies

app = Flask(__name__)
app.debug = True

@app.route("/")
def index():
    entries = get_entries()
    return render_template("home.html", entries=entries)

#TECHSOC
@app.route("/tech")
def tech():
    entries = get_entries(filter_soc="tec")
    return render_template("tech.html", entries=entries)

@app.route("/tech/info")
def tech_info():
    return render_template("tech_info.html")

@app.route("/rob")
def robotics():
    entries = get_entries(filter_clb="rob")
    return render_template("rob.html", entries=entries)

@app.route("/ele")
def electronics():
    entries = get_entries(filter_clb="rob")
    return render_template("ele.html", entries=entries)

@app.route("/pro")
def programming():
    entries = get_entries(filter_clb="pro")
    return render_template("pro.html", entries=entries)

@app.route("/mad")
def mad():
    entries = get_entries(filter_clb="mad")
    return render_template("mad.html", entries=entries)

@app.route("/stac")
def stac():
    entries = get_entries(filter_clb="stac")
    return render_template("stac.html", entries=entries)

@app.route("/ene")
def energy():
    entries = get_entries(filter_clb="ene")
    return render_template("ene.html", entries=entries)

@app.route("/scri")
def scri():
    entries = get_entries(filter_clb="scri")
    return render_template("scri.html", entries=entries)


#litsoc

@app.route("/lit")
def literary():
    entries = get_entries(filter_soc="lit")
    return render_template("literary.html", entries=entries)

@app.route("/lit/info")
def literary_info():
    return render_template("literary_info.html")

@app.route("/edl")
def edls():
    entries = get_entries(filter_clb="edl")
    return render_template("edl.html", entries=entries)

@app.route("/mag")
def magazine():
    entries = get_entries(filter_clb="mag")
    return render_template("mag.html", entries=entries)




#cultsoc
@app.route("/cult")
def cultural():
    entries = get_entries(filter_soc="cul")
    return render_template("cult.html", entries=entries)

@app.route("/cult/info")
def cult_info():
    return render_template("cult_info.html")

@app.route("/mus")
def music():
    entries = get_entries(filter_clb="mus")
    return render_template("mus.html", entries=entries)

@app.route("/dan")
def dance():
    entries = get_entries(filter_clb="dan")
    return render_template("dan.html", entries=entries)

@app.route("/dra")
def drama():
    entries = get_entries(filter_clb="dra")
    return render_template("dra.html", entries=entries)

@app.route("/pho")
def photography():
    entries = get_entries(filter_clb="pho")
    return render_template("pho.html", entries=entries)

@app.route("/pm")
def pm():
    entries = get_entries(filter_clb="pm")
    return render_template("pm.html", entries=entries)

@app.route("/art")
def art():
    entries = get_entries(filter_clb="art")
    return render_template("art.html", entries=entries)


#sports
@app.route("/sports")
def sports():
    entries = get_entries(filter_soc="spo")
    return render_template("sports.html", entries=entries)

@app.route("/sports/info")
def sports_info():
    return render_template("sports_info.html")


@app.route("/cri")
def cricket():
    entries = get_entries(filter_clb="cri")
    return render_template("cri.html", entries=entries)

@app.route("/foo")
def football():
    entries = get_entries(filter_clb="foo")
    return render_template("foo.html", entries=entries)

@app.route("/bas")
def basketball():
    entries = get_entries(filter_clb="bas")
    return render_template("bas.html", entries=entries)

@app.route("/bad")
def badminton():
    entries = get_entries(filter_clb="bad")
    return render_template("bad.html", entries=entries)

@app.route("/tt")
def tt():
    entries = get_entries(filter_clb="tt")
    return render_template("tt.html", entries=entries)

@app.route("/vol")
def volleyball():
    entries = get_entries(filter_clb="vol")
    return render_template("vol.html", entries=entries)

@app.route("/hoc")
def hockey():
    entries = get_entries(filter_clb="hoc")
    return render_template("hoc.html", entries=entries)


@app.route("/ath")
def athletics():
    entries = get_entries(filter_clb="ath")
    return render_template("ath.html", entries=entries)

#acad           
@app.route("/acad")
def academics():
    entries = get_entries(filter_soc="aca")
    return render_template("acad.html", entries=entries)

@app.route("/acad/info")
def acad_info():
    return render_template("acad_info.html")

#nss
@app.route("/nss")
def nss():
    entries = get_entries(filter_soc="nss")
    return render_template("nss.html", entries=entries)


@app.route("/nss/info")
def nss_info():
    return render_template("nss_info.html")



@app.route("/nso")
def nso():
    return render_template("nso_info.html")


@app.route("/contacts")
def contacts():
    
    return render_template("contacts.html")

@app.route("/gallery")
def gallery():
    
    return render_template("gallery.html")



@app.route("/hos/")
def hos():
    entries = get_entries(filter_soc="hos")
    return render_template("hos_info.html",entries=entries)

@app.route("/hk/")
def hk():
    return render_template("hk_info.html")


@app.route("/entry")
def entry():
    entry_hex = request.args.get("id")
    entry_raw = unhexlify(entry_hex)

    entries_raw = get_entries_raw()
    entries = get_entries()
    if entry_raw in entries_raw:
        date, society, club = get_entry_mdata(entry_raw)
        with open(entry_raw) as doc:
            entry = [markdown(doc.read()), societies[society], date]

        print(entry)

        return render_template("entry.html",
                               entry=entry,
                               recent_entries=entries[:4])

    else:
        return "Problem with retrieving entry."

if __name__ == '__main__':
    app.run()
