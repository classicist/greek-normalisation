PROCLITICS = [
    "ὁ", "ἡ", "οἱ", "αἱ",
    "ἐν", "εἰς", "ἐξ", "ἐκ",
    "εἰ", "ὡς",
    "οὐ", "οὐκ", "οὐχ",
]

ENCLITICS = [
    # personal pronouns
    "μου", "μοι", "με",
    "σου", "σοι", "σε",

    # indefinite pronouns
    "τὶς", "τὶ", "τινός", "τινί", "τινά", "τινές", "τινάς", "τινῶν", "τισίν",
    "τισί",

    # indefinite adverbs
    "πού", "ποτέ", "πώ", "πώς",

    # dissyllabic forms of εἰμί
    "εἰμί", "εἰσίν", "εἰσί", "ἐσμέν", "ἐστέ", "ἐστίν", "ἐστί",

    # dissyllabic forms of φημί
    "φησίν", "φημί", "φασίν",

    # certain particles
    "γέ", "τέ", "τοι",
]


ELISION = {
    "ἀλλ’": "ἀλλά",
    "ἀνθ’": "ἀντί",
    "ἀπ’": "ἀπό",
    "ἀφ’": "ἀπό",
    "γένοιτ’": "γένοιτο",
    "δ’": "δέ",
    "δι’": "διά",
    "δύναιτ’": "δύναιτο",
    "εἶτ’": "εἶτα",  # @@@
    "ἐπ’": "ἐπί",
    "ἐφ’": "ἐπί",
    "ἡγοῖντ’": "ἡγοῖντο",
    "ἵν’": "ἵνα",
    "κατ’": "κατά",
    "καθ’": "κατά",
    "μηδ’": "μηδέ",
    "μετ’": "μετά",
    "μεθ’": "μετά",
    "ὅτ’": "ὅτε",
    "οὐδ’": "οὐδέ",
    "πάνθ’": "πάντα",
    "πάντ’": "πάντα",
    "παρ’": "παρά",
    "ποτ’": "ποτε",
    "ταῦθ’": "ταῦτα",
    "τοῦτ’": "τοῦτο",
    "ὑπ’": "ὑπό",
    "ὑφ’": "ὑπό",
}


MOVABLE = {
    "ἐξ": "ἐκ",

    "οὐκ": "οὐ",
    "οὐχ": "οὐ",
}


PROPER_NOUNS = {
    "Αγγ",
    "Ἀθῆναι",
    "Αἴγυπτος",
    "Ἀλέξιον",
    "Ἀλέξιος",
    "Ἀλεξίου",
    "Ἀντιοχεία",
    "Ἀντιοχείᾳ",
    "Ἀντιόχεια",
    "Ἀντιόχειαν",
    "Ἀντιοχείας",
    "Ἀραβία",
    "Ἀραβίᾳ",
    "Ἀσία",
    "Ἀσίᾳ",
    "Ἀτλαντικόν",
    "Ἀφρικῇ",
    "Βρεταννία",
    "Βρεττανία",
    "Γαλλία",
    "Γαλλίᾳ",
    "Γερμανία",
    "Γερμανίᾳ",
    "Γηργόριος",
    "Γηργόριους",
    "Γρη",
    "Γρηγόριον",
    "Γρηγόριος",
    "Γρηγορίου",
    "Γρηγόριου",
    "Γρηγορίῳ",
    "Γρηγρορίου",
    "Γρηρόριος",
    "Δῆλος",
    "Δημήρτιος",
    "Δημήτριε",
    "Δημήτριον",
    "Δημήτριος",
    "Δημητρίου",
    "Δικαιόπολις",
    "Εἰρήνη",
    "Εἰρήνης",
    "Ἑλλάδι",
    "Ἑλλάς",
    "Ἑλληνικά",
    "Ἑλληνικαί",
    "Ἑλληνική",
    "Ἑλληνικοί",
    "Ἑλληνικόν",
    "Ἑλληνικός",
    "Εὔβοια",
    "Εὐγενία",
    "Εὐγενίᾳ",
    "Εὐγενίαν",
    "Εὐγενίας",
    "Εὐρώπῃ",
    "Ζεύς",
    "Ἡρακλείδης",
    "Θύμβρις",
    "Ἱεροσόλυμα",
    "Ἰησοῦς",
    "Ἱσπανία",
    "Ἴστρος",
    "Ἰταλία",
    "Ἰταλίᾳ",
    "Κεφαλαῖον",
    "Κεφάλαιον",
    "Κίλισσα",
    "Κιλίσσης",
    "Κρήτη",
    "Κωνσταντινούπολις",
    "Λέσβος",
    "Λῆμνος",
    "Μακ",
    "Μακάριον",
    "Μακάριος",
    "Μακαρίῳ",
    "Μαρ",
    "Μάρκος",
    "Νάξος",
    "Νεῖλος",
    "Ξαν",
    "Ξανθία",
    "Ξανθίᾳ",
    "Ξανθίας",
    "Ὀρόντες",
    "Ὀρόντης",
    "Πιερίᾳ",
    "Ῥαβέννα",
    "Ῥῆνος",
    "Ῥόδος",
    "Ῥωμαϊκά",
    "Ῥωμαϊκαί",
    "Ῥωμαϊκή",
    "Ῥωμαϊκῇ",
    "Ῥωμαϊκόν",
    "Ῥωμαϊκός",
    "Ῥώμη",
    "Ῥώμην",
    "Σάμος",
    "Σελεύκεια",
    "Σελεύκειαν",
    "Σελεύκιαν",
    "Σελευκίας",
    "Σικελία",
    "Σοσίαν",
    "Σοφία",
    "Σοφίας",
    "Σπαρτή",
    "Σπάρτη",
    "Σύρα",
    "Συρία",
    "Συρίᾳ",
    "Συριακαί",
    "Συριακή",
    "Συριακός",
    "Συρίας",
    "Σως",
    "Σωσία",
    "Σωσίαν",
    "Σωσίας",
    "Σωσίου",
    "Σωφία",
    "Σωφίαν",
    "Τρο",
    "Τροχίλε",
    "Τροχίλον",
    "Τροχίλος",
    "Χίος",
    "Χριστιανῶν",
    "Χριστός",
    "Χριστοῦ",
}


SPECIAL_CASES = {
    "πο-",
    "-τα-",
    "-μος",

    "Α",
    "Β",
    "Γ",
    "Δ",

    "Αγγ",
    "Γρη",
    "Μακ",
    "Μαρ",
    "Ξαν",
    "Σως",
    "Τρο",

    # "#",
    # "ἀλλα",
    # "δε",
    # "καἰ",
    # "στ",
}
