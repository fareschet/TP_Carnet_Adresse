# -*- coding: utf-8 -*-

import sqlite3

class ContactModel:

    def __init__(self, db_name='Controleur/carnet.db'):
        self.conn = sqlite3.connect(db_name)
        self.creer_table()

    def creer_table(self):
        query = '''
            CREATE TABLE IF NOT EXISTS Contact (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nom TEXT,
                prenom TEXT,
                telephone TEXT,
                email TEXT
            )
        '''
        self.conn.execute(query)
        self.conn.commit()

    def ajouter_contact(self, nom, prenom, telephone, email):
        query = '''
            INSERT INTO Contact (nom, prenom, telephone, email)
            VALUES (?, ?, ?, ?)
        '''
        self.conn.execute(query, (nom, prenom, telephone, email))
        self.conn.commit()

    def modifier_contact(self, contact_id, nom, prenom, telephone, email):
        query = '''
            UPDATE Contact
            SET nom=?, prenom=?, telephone=?, email=?
            WHERE id=?
        '''
        self.conn.execute(query, (nom, prenom, telephone, email, contact_id))
        self.conn.commit()

    def supprimer_contact(self, contact_id):
        query = '''
            DELETE FROM Contact
            WHERE id=?
        '''
        self.conn.execute(query, (contact_id,))
        self.conn.commit()

    def afficher_contacts(self):
        query = 'SELECT * FROM Contact'
        cursor = self.conn.execute(query)
        contacts = cursor.fetchall()
        self.conn.commit()
        return contacts

    def chercher_contact_model(self, champ, value):
        query = f'''
            SELECT * FROM Contact
            WHERE {champ} = ?
        '''
        cursor = self.conn.execute(query, (value,))
        contacts = cursor.fetchall()
        self.conn.commit()
        return contacts

