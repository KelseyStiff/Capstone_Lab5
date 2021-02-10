from peewee import *
db = SqliteDatabase('jugglers.sqlite')

class Juggler(Model):
    name = CharField()
    country = CharField()
    num_of_catches = IntegerField()

    class Meta:
        database = db

    def __str__(self):
        return f'{self.id}: {self.name}, {self.country}, {self.num_of_catches}'

db.connect()
db.create_tables([Juggler])

def add_example_data():
    janne = Juggler(name ='Janne Mustonen', country='Finland' , num_of_catches='98')
    janne.save()
    ian = Juggler(name='Ian Stewart', country='Canada' , num_of_catches='94')
    ian.save()
    aaron = Juggler(name = 'Aaron Gregg', country = 'Canada' , num_of_catches = '88')
    aaron.save()
    chad = Juggler(name = 'Chad Taylor', country = 'USA' , num_of_catches = '78')
    chad.save()




def add_data(juggler_name, juggler_country,juggler_catches):
    juggler_data = Juggler(name = juggler_name, country =juggler_country , num_of_catches = juggler_catches)
    juggler_data.save()


def display_data():
    jugglers = Juggler.select()
    print('\n')
    for juggler in jugglers:
        print(juggler)
    print('\n')

def delete_data(delete_juggler_name):
    Juggler.delete().where(Juggler.name == delete_juggler_name).execute()

def delete_table():
    Juggler.delete().execute()

def update_data(edit_juggler):
    update_field = input('Enter name to update name, country to update country,catches to update catches: ')
    if update_field == 'name':
        updated_name = input('Enter new name: ')
        Juggler.update(name=updated_name).where(Juggler.name == edit_juggler).execute()

    if update_field == 'country':
        updated_country = input('Enter new country: ')
        Juggler.update(country=updated_country).where(Juggler.name == edit_juggler).execute()

    if update_field == 'catches':
        updated_catches = input('Enter new catches: ')
        Juggler.update(num_of_catches=updated_catches).where(Juggler.name == edit_juggler).execute()



def main():
    while True:

        delete_table()


        add_example_data()

        #shows db and table are created with example data
        display_data()

        #user input for adding new data 
        print('\n**ADD NEW JUGGLER RECORD**\n')
        juggler_name = input('Enter jugglers name or enter to quit: ')
        if not juggler_name:
            break
        juggler_country = input(f'Enter a country for {juggler_name}: ')
        juggler_catches = input(f'Enter number of catches for {juggler_name}: ')

        # adds data to db
        add_data(juggler_name, juggler_country,juggler_catches)

        # display data agian to show new addition
        display_data()


        delete_juggler_name = input('Enter a jugglers full name to DELETE: ')
        delete_data(delete_juggler_name)

        #shows deletion
        display_data()

        edit_juggler = input('Enter a jugglers name to EDIT: ')
        update_data(edit_juggler)

        #shows edits made
        display_data()

        break


    



if __name__ == '__main__':
    main()


