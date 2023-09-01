# -*- coding: utf-8 -*-
# 70% de ce design est réalisé par PYQT Designer
from PyQt6.QtCore import (QCoreApplication, QMetaObject, QRect, QRegularExpression, QTimer)
from PyQt6.QtGui import (QFont, QRegularExpressionValidator, QPixmap)
from PyQt6.QtWidgets import (QGroupBox, QLabel, QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
                             QPushButton, QTableWidget, QTableWidgetItem, QWidget)
from Controleur import ContactControleur

class FenetreCarnetAdresse(QMainWindow):
    def setupUi(self, Fenetre_Carnet_Adresse):
        self.__id = 0
        if not Fenetre_Carnet_Adresse.objectName():
            Fenetre_Carnet_Adresse.setObjectName(u"Fenetre_Carnet_Adresse")
        Fenetre_Carnet_Adresse.setEnabled(True)
        Fenetre_Carnet_Adresse.setFixedSize(695, 660)
        self.central = QWidget(Fenetre_Carnet_Adresse)
        self.central.setStyleSheet("background-color: #1a6985; z-index: -1;")
        self.central.resize(695, 660)

        self.centralwidget = QWidget(Fenetre_Carnet_Adresse)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox_Contact = QGroupBox(self.centralwidget)
        self.groupBox_Contact.setObjectName(u"groupBox_Contact")
        self.groupBox_Contact.setGeometry(QRect(20, 20, 311, 241))
        font = QFont()
        font.setBold(False)
        self.groupBox_Contact.setFont(font)

        self.NomLbl = QLabel(self.groupBox_Contact)
        self.NomLbl.setObjectName(u"NomLbl")
        self.NomLbl.setGeometry(QRect(20, 30, 49, 16))

        self.PrenomLbl = QLabel(self.groupBox_Contact)
        self.PrenomLbl.setObjectName(u"PrenomLbl")
        self.PrenomLbl.setGeometry(QRect(20, 70, 49, 16))

        self.TelephoneLbl = QLabel(self.groupBox_Contact)
        self.TelephoneLbl.setObjectName(u"TelephoneLbl")
        self.TelephoneLbl.setGeometry(QRect(20, 110, 200, 16))

        self.EmailLbl = QLabel(self.groupBox_Contact)
        self.EmailLbl.setObjectName(u"EmailLbl")
        self.EmailLbl.setGeometry(QRect(20, 150, 49, 16))

        self.NomLine = QLineEdit(self.groupBox_Contact)
        self.NomLine.setObjectName(u"NomLine")
        self.NomLine.setGeometry(QRect(90, 30, 158, 21))

        self.PrenomLine = QLineEdit(self.groupBox_Contact)
        self.PrenomLine.setObjectName(u"PrenomLine")
        self.PrenomLine.setGeometry(QRect(90, 70, 158, 21))

        self.TelephoneLine = QLineEdit(self.groupBox_Contact)
        self.TelephoneLine.setObjectName(u"TelephoneLine")
        self.TelephoneLine.setGeometry(QRect(90, 110, 158, 21))
        self.TelephoneLine.setPlaceholderText("000-000-0000")

        self.EmailLine = QLineEdit(self.groupBox_Contact)
        self.EmailLine.setObjectName(u"EmailLine")
        self.EmailLine.setGeometry(QRect(90, 150, 158, 21))
        self.EmailLine.setPlaceholderText("exemple@domaine.com")

        font1 = QFont()
        font1.setBold(True)

        self.ajout_modifier_btn = QPushButton(self.groupBox_Contact)
        self.ajout_modifier_btn.setObjectName(u"ajout_modifier_btn")
        self.ajout_modifier_btn.setGeometry(QRect(90, 190, 75, 24))
        self.ajout_modifier_btn.clicked.connect(self.ajouter_modifier_contact)
        self.ajout_modifier_btn.setFont(font1)

        self.effacer_supprimer_btn = QPushButton(self.groupBox_Contact)
        self.effacer_supprimer_btn.setObjectName(u"effacer_supprimer_btn")
        self.effacer_supprimer_btn.setGeometry(QRect(170, 190, 82, 24))
        self.effacer_supprimer_btn.clicked.connect(self.supprimer_effacer_contact)
        self.effacer_supprimer_btn.setFont(font1)

        self.groupBox_AfficherContact = QGroupBox(self.centralwidget)
        self.groupBox_AfficherContact.setObjectName(u"groupBox_AfficherContact")
        self.groupBox_AfficherContact.setGeometry(QRect(20, 390, 631, 241))

        self.tableContacts = QTableWidget(self.groupBox_AfficherContact)
        if (self.tableContacts.columnCount() < 5):
            self.tableContacts.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableContacts.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableContacts.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableContacts.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableContacts.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableContacts.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableContacts.setObjectName(u"tableContacts")
        self.tableContacts.setGeometry(QRect(20, 30, 592, 192))
        self.tableContacts.setColumnWidth(0, 50)
        self.tableContacts.setColumnWidth(1, 120)
        self.tableContacts.setColumnWidth(2, 120)
        self.tableContacts.setColumnWidth(3, 128)
        self.tableContacts.setColumnWidth(4, 160)
        self.afficher_liste_contact(self.tableContacts)
        self.tableContacts.cellClicked.connect(self.afficher_ligne_selectionnee_table)

        self.chercherLine = QLineEdit(self.centralwidget)
        self.chercherLine.setObjectName(u"chercherLine")
        self.chercherLine.setGeometry(QRect(20, 320, 171, 21))
        self.chercherLine.setFont(font)

        self.chercher_btn = QPushButton(self.centralwidget)
        self.chercher_btn.setObjectName(u"chercher_btn")
        self.chercher_btn.setGeometry(QRect(210, 320, 75, 24))
        self.chercher_btn.setFont(font1)
        self.chercher_btn.clicked.connect(self.chercher_contact)

        self.annuler_chercher_btn = QPushButton(self.centralwidget)
        self.annuler_chercher_btn.setObjectName(u"chercher_btn")
        self.annuler_chercher_btn.setText("Annuler")
        self.annuler_chercher_btn.setGeometry(QRect(210, 355, 75, 24))
        self.annuler_chercher_btn.setFont(font1)
        self.annuler_chercher_btn.clicked.connect(self.annuler_chercher_contact)
        self.annuler_chercher_btn.setVisible(False)

        self.msgLbl = QLabel(self.centralwidget)
        self.msgLbl.setObjectName(u"msgLbl")
        self.msgLbl.setGeometry(QRect(20, 355, 155, 21))
        self.msgLbl.setVisible(False)

        self.list_choix_champs = QListWidget(self.centralwidget)
        QListWidgetItem(self.list_choix_champs)
        QListWidgetItem(self.list_choix_champs)
        QListWidgetItem(self.list_choix_champs)
        QListWidgetItem(self.list_choix_champs)
        QListWidgetItem(self.list_choix_champs)
        self.list_choix_champs.setObjectName(u"list_choix_champs")
        self.list_choix_champs.setGeometry(QRect(20, 280, 261, 28))
        self.list_choix_champs.setFont(font)

        self.groupBox_image = QGroupBox(self.centralwidget)
        self.groupBox_image.setObjectName(u"groupBox_image")
        self.groupBox_image.setGeometry(QRect(350, 20, 300, 360))
        self.image = QLabel(self.groupBox_image)
        self.image.setPixmap(QPixmap("./images/phone-book.png"))
        self.image.setScaledContents(True)
        self.image.setGeometry(QRect(30, 60, 250, 250))

        self.titre = QLabel(self.groupBox_image)
        self.titre.setText("Carnet d'adresse")
        self.titre.setStyleSheet(
            "font-family: Comic Sans MS, cursive, sans-serif; font-size: 25px; letter-spacing: -0.2px; word-spacing: 0.6px;color: #25be7d; font-weight: 700;text-decoration: none;font-style: italic;font-variant: normal;ext-transform: none;")
        self.titre.setGeometry(QRect(40, 28, 250, 25))

        self.copyright = QLabel(self.groupBox_image)
        self.copyright.setText("Crée par: Fares, Nabil, Hamza, Madi")
        self.copyright.setStyleSheet("background-color: #144d69; color: #beb425;font-style: italic; padding: 1px; border-radius: 4px;")
        self.copyright.setGeometry(QRect(30, 315, 230, 25))

        Fenetre_Carnet_Adresse.setCentralWidget(self.centralwidget)
        self.retranslateUi(Fenetre_Carnet_Adresse)
        QMetaObject.connectSlotsByName(Fenetre_Carnet_Adresse)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("Fenetre_Carnet_Adresse", u"Carnet d'Adresse", None))
        self.NomLbl.setText(QCoreApplication.translate("Fenetre_Carnet_Adresse", u"Nom:", None))
        self.PrenomLbl.setText(QCoreApplication.translate("Fenetre_Carnet_Adresse", u"Pr\u00e9nom:", None))
        self.TelephoneLbl.setText(QCoreApplication.translate("Fenetre_Carnet_Adresse", u"T\u00e9l\u00e9phone:", None))
        self.EmailLbl.setText(QCoreApplication.translate("Fenetre_Carnet_Adresse", u"Email:", None))
        self.ajout_modifier_btn.setText(QCoreApplication.translate("Fenetre_Carnet_Adresse", u"Ajouter", None))
        self.effacer_supprimer_btn.setText(QCoreApplication.translate("Fenetre_Carnet_Adresse", u"Effacer", None))
        ___qtablewidgetitem = self.tableContacts.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Fenetre_Carnet_Adresse", u"ID", None));
        ___qtablewidgetitem1 = self.tableContacts.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Fenetre_Carnet_Adresse", u"Nom", None));
        ___qtablewidgetitem2 = self.tableContacts.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Fenetre_Carnet_Adresse", u"Pr\u00e9nom", None));
        ___qtablewidgetitem3 = self.tableContacts.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(
            QCoreApplication.translate("Fenetre_Carnet_Adresse", u"T\u00e9l\u00e9phone", None));
        ___qtablewidgetitem4 = self.tableContacts.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Fenetre_Carnet_Adresse", u"Email", None));
        self.chercher_btn.setText(QCoreApplication.translate("Fenetre_Carnet_Adresse", u"Chercher", None))

        __sortingEnabled = self.list_choix_champs.isSortingEnabled()
        self.list_choix_champs.setSortingEnabled(False)
        ___qlistwidgetitem = self.list_choix_champs.item(0)
        ___qlistwidgetitem.setText(
            QCoreApplication.translate("Fenetre_Carnet_Adresse", u"S\u00e9l\u00e9ctionner un champ pour la recherche",
                                       None));
        ___qlistwidgetitem1 = self.list_choix_champs.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("Fenetre_Carnet_Adresse", u"Nom", None));
        ___qlistwidgetitem2 = self.list_choix_champs.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("Fenetre_Carnet_Adresse", u"Pr\u00e9nom", None));
        ___qlistwidgetitem3 = self.list_choix_champs.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("Fenetre_Carnet_Adresse", u"T\u00e9l\u00e9phone", None));
        ___qlistwidgetitem4 = self.list_choix_champs.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("Fenetre_Carnet_Adresse", u"Email", None));
        self.list_choix_champs.setSortingEnabled(__sortingEnabled)

    def ajouter_modifier_contact(self):
        btn = self.ajout_modifier_btn.text()
        nom = self.NomLine.text()
        prenom = self.PrenomLine.text()
        telephone = self.TelephoneLine.text()
        email = self.EmailLine.text()
        if nom != "" and prenom != "" and telephone != "" and email != "":
            if btn == "Ajouter":
                verifier_telephone = self.verifier_numero_telephone()
                verifier_email = self.verifier_email()
                if verifier_telephone and verifier_email:
                    ContactControleur.ContactController().ajouter_contact(nom, prenom, telephone, email, self)
            else:
                verifier_telephone = self.verifier_numero_telephone()
                verifier_email = self.verifier_email()
                if verifier_telephone and verifier_email:
                    ContactControleur.ContactController().modifier_contact(self.__id, nom, prenom, telephone, email,
                                                                           self)
        self.afficher_liste_contact(self.tableContacts)

    def supprimer_effacer_contact(self):
        btn = self.effacer_supprimer_btn.text()
        if btn == "Supprimer":
            ContactControleur.ContactController().supprimer_contact(self.__id, self)
        else:
            self.msgLbl.setVisible(False)
            self.NomLine.clear()
            self.PrenomLine.clear()
            self.TelephoneLine.clear()
            self.EmailLine.clear()
            self.TelephoneLine.setStyleSheet("background-color: #FFF;")
            self.EmailLine.setStyleSheet("background-color: #FFF;")
        self.afficher_liste_contact(self.tableContacts)

    def chercher_contact(self):
        btn = self.chercher_btn.text()
        contenu = self.chercherLine.text()
        item = self.list_choix_champs.selectedItems()
        if item:
            if btn == "Chercher":
                self.desactiver_pour_la_recherche()
                choix = self.list_choix_champs.currentItem().text()

                if choix == "Séléctionner un champ pour la recherche" or contenu == "":
                    self.annuler_chercher_contact()
                elif choix == "Nom":
                    ContactControleur.ContactController().chercher_contact_controleur("nom", contenu, self.tableContacts, self)
                elif choix == "Prénom":
                    ContactControleur.ContactController().chercher_contact_controleur("prenom", contenu, self.tableContacts, self)
                elif choix == "Téléphone":
                    ContactControleur.ContactController().chercher_contact_controleur("telephone", contenu, self.tableContacts, self)
                elif choix == "Email":
                    ContactControleur.ContactController().chercher_contact_controleur("email", contenu, self.tableContacts, self)

    def annuler_chercher_contact(self):
        self.NomLine.setEnabled(True)
        self.PrenomLine.setEnabled(True)
        self.TelephoneLine.setEnabled(True)
        self.EmailLine.setEnabled(True)
        self.ajout_modifier_btn.setEnabled(True)
        self.effacer_supprimer_btn.setEnabled(True)
        self.afficher_liste_contact(self.tableContacts)
        self.annuler_chercher_btn.setVisible(False)
        self.chercherLine.clear()
        self.msgLbl.setVisible(False)
        self.NomLine.clear()
        self.PrenomLine.clear()
        self.TelephoneLine.clear()
        self.EmailLine.clear()
        self.ajout_modifier_btn.setText("Ajouter")
        self.effacer_supprimer_btn.setText("Effacer")

    def desactiver_pour_la_recherche(self):
        self.annuler_chercher_btn.setVisible(True)
        self.NomLine.setEnabled(False)
        self.PrenomLine.setEnabled(False)
        self.TelephoneLine.setEnabled(False)
        self.EmailLine.setEnabled(False)
        self.ajout_modifier_btn.setEnabled(False)
        self.effacer_supprimer_btn.setEnabled(False)
        self.NomLine.clear()
        self.PrenomLine.clear()
        self.TelephoneLine.clear()
        self.EmailLine.clear()
        self.ajout_modifier_btn.setText("Ajouter")
        self.effacer_supprimer_btn.setText("Effacer")

    def afficher_liste_contact(self, table):
        ContactControleur.ContactController().afficher_contacts(table)

    def afficher_ligne_selectionnee_table(self, row):
        id_item = self.tableContacts.item(row, 0)
        nom_item = self.tableContacts.item(row, 1)
        prenom_item = self.tableContacts.item(row, 2)
        telephone_item = self.tableContacts.item(row, 3)
        email_item = self.tableContacts.item(row, 4)
        self.__id = int(id_item.text())
        self.NomLine.setEnabled(True)
        self.PrenomLine.setEnabled(True)
        self.TelephoneLine.setEnabled(True)
        self.EmailLine.setEnabled(True)
        self.ajout_modifier_btn.setEnabled(True)
        self.effacer_supprimer_btn.setEnabled(True)
        self.annuler_chercher_btn.setVisible(False)
        self.chercherLine.clear()
        self.msgLbl.setVisible(False)
        if nom_item and prenom_item and prenom_item and telephone_item and email_item:
            self.NomLine.setText(nom_item.text())
            self.PrenomLine.setText(prenom_item.text())
            self.TelephoneLine.setText(telephone_item.text())
            self.EmailLine.setText(email_item.text())
            self.ajout_modifier_btn.setText("Modifier")
            self.effacer_supprimer_btn.setText("Supprimer")
            self.annuler_chercher_btn.setVisible(True)

    def verifier_numero_telephone(self):
        regex = QRegularExpression(r"\d{3}-\d{3}-\d{4}")
        validator = QRegularExpressionValidator(regex)
        self.TelephoneLine.setValidator(validator)
        if self.TelephoneLine.hasAcceptableInput():
            self.msgLbl.setVisible(False)
            self.TelephoneLine.setStyleSheet("background-color: #FFF;")
            self.TelephoneLine.raise_()
            return True
        else:
            self.msgLbl.setVisible(True)
            self.msgLbl.setText("Le numéro est incorrect!")
            self.msgLbl.setStyleSheet("color: #FFF;")
            self.TelephoneLine.setStyleSheet("background-color: #873e23;")
            self.TelephoneLine.raise_()
            self.visibilite_message_erreur()
            return False

    def verifier_email(self):
        verifier_telephone = self.verifier_numero_telephone()
        if verifier_telephone:
            regex = QRegularExpression(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$")
            validator = QRegularExpressionValidator(regex)
            self.EmailLine.setValidator(validator)
            if self.EmailLine.hasAcceptableInput():
                self.msgLbl.setVisible(False)
                self.EmailLine.setStyleSheet("background-color: #FFF;")
                self.EmailLine.raise_()
                return True
            else:
                self.msgLbl.setVisible(True)
                self.msgLbl.setText("L'email est incorrect!")
                self.msgLbl.setStyleSheet("color: #FFF;")
                self.EmailLine.setStyleSheet("background-color: #873e23;")
                self.EmailLine.raise_()
                self.visibilite_message_erreur()
                return False

    def visibilite_message_erreur(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.timing)
        self.timer.start(5000)

    def timing(self):
        self.timer.stop()
        self.msgLbl.setVisible(False)
