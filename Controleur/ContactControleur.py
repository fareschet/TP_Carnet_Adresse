# -*- coding: utf-8 -*-
from Model import ContactModel
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QTableWidgetItem
class ContactController:
    def __init__(self):
        self.model = ContactModel.ContactModel()

    def ajouter_contact(self, nom, prenom, telephone, email, contact):
        self.model.ajouter_contact(nom, prenom, telephone, email)
        contact.msgLbl.setVisible(True)
        contact.msgLbl.setText("Ajout avec succès!")
        contact.msgLbl.setStyleSheet("color: #bea925;")
        contact.NomLine.clear()
        contact.PrenomLine.clear()
        contact.TelephoneLine.clear()
        contact.EmailLine.clear()
        contact.visibilite_message_erreur()

    def modifier_contact(self, contact_id, nom, prenom, telephone, email, contact):
        self.model.modifier_contact(contact_id, nom, prenom, telephone, email)
        contact.msgLbl.setVisible(True)
        contact.msgLbl.setText("Modification avec succès!")
        contact.msgLbl.setStyleSheet("color: #bea925;")
        contact.NomLine.clear()
        contact.PrenomLine.clear()
        contact.TelephoneLine.clear()
        contact.EmailLine.clear()
        contact.ajout_modifier_btn.setText("Ajouter")
        contact.effacer_supprimer_btn.setText("Effacer")
        contact.visibilite_message_erreur()
        contact.annuler_chercher_btn.setVisible(False)

    def supprimer_contact(self, contact_id, contact):
        self.model.supprimer_contact(contact_id)
        contact.msgLbl.setVisible(True)
        contact.msgLbl.setText("Suppression avec succès!")
        contact.msgLbl.setStyleSheet("color: #bea925;")
        contact.NomLine.clear()
        contact.PrenomLine.clear()
        contact.TelephoneLine.clear()
        contact.EmailLine.clear()
        contact.ajout_modifier_btn.setText("Ajouter")
        contact.effacer_supprimer_btn.setText("Effacer")
        contact.visibilite_message_erreur()
        contact.annuler_chercher_btn.setVisible(False)

    def afficher_contacts(self, contact_Table):
        self.data = self.model.afficher_contacts()
        contact_Table.setRowCount(len(self.data))
        if len(self.data) > 0:
            row = 0
            for contact in self.data:
                contact_Table.setItem(row, 0, QTableWidgetItem(str(contact[0])))
                contact_Table.item(row, 0).setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                contact_Table.setItem(row, 1, QTableWidgetItem(contact[1]))
                contact_Table.item(row, 1).setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                contact_Table.setItem(row, 2, QTableWidgetItem(contact[2]))
                contact_Table.item(row, 2).setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                contact_Table.setItem(row, 3, QTableWidgetItem(contact[3]))
                contact_Table.item(row, 3).setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                contact_Table.setItem(row, 4, QTableWidgetItem(contact[4]))
                contact_Table.item(row, 4).setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                row += 1

    def chercher_contact_controleur(self, champ, value, contact_Table, contact):
        self.data = self.model.chercher_contact_model(champ, value)
        contact_Table.setRowCount(len(self.data))
        if len(self.data) > 0:
            contact.msgLbl.setVisible(False)
            row = 0
            for contact in self.data:
                contact_Table.setItem(row, 0, QTableWidgetItem(str(contact[0])))
                contact_Table.item(row, 0).setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                contact_Table.setItem(row, 1, QTableWidgetItem(contact[1]))
                contact_Table.item(row, 1).setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                contact_Table.setItem(row, 2, QTableWidgetItem(contact[2]))
                contact_Table.item(row, 2).setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                contact_Table.setItem(row, 3, QTableWidgetItem(contact[3]))
                contact_Table.item(row, 3).setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                contact_Table.setItem(row, 4, QTableWidgetItem(contact[4]))
                contact_Table.item(row, 4).setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                row += 1

        else:
            contact.annuler_chercher_btn.setEnabled(True)
            contact.msgLbl.setVisible(True)
            contact.msgLbl.setText("Le contact n'existe pas!")
            contact.msgLbl.setStyleSheet("color: #FFF;")
            contact.visibilite_message_erreur()
