import subprocess as sp
import pymysql
import pymysql.cursors
from datetime import datetime
from datetime import date

def addperson():
    try:
        row={}
        print("Enter details of Personality: ")
        row["PersonName"] = input("Name: ")
        row["DateOfBirth"] = input("DateOfBirth: ")
        row["Gender"] = input("Gender: ")
        if row["Gender"]!='M' and row["Gender"]!='F':
            print("invalid Gender")
            return
        row["Profession"] = input("Profession: ")
        if row["Profession"] == 'ACTOR':
            c = int(input("Please give avgpaycheck: "))
        elif row["Profession"] == 'DIRECTOR':
            c = input("Please select Favourite Genre: ")
        elif row["Profession"] == 'PRODUCER':
            c = int(input("Please select avgbudget: "))
        else:
            print("INVALID PROFESSION")
            return
                
        row["HouseNo"] = input("HouseNo: ")
        row["Street"] = input("Street: ")
        row["City"] = input("City: ")
        query = "INSERT INTO MAJOR_PERSONALITIES(PersonName,DateOfBirth,Gender,Profession,HouseNo,Street,City) VALUES('%s', '%s', '%s','%s','%s','%s','%s')" %(row["PersonName"], row["DateOfBirth"], row["Gender"],row["Profession"] ,row["HouseNo"],row["Street"],row["City"])
        cur.execute(query)
        con.commit()
        print("Inserted Into MAJOR_PERSONALITIES table")
        if row["Profession"] == 'ACTOR':
            query = "SELECT PersonID FROM MAJOR_PERSONALITIES ORDER BY PersonID DESC LIMIT 1"
            cur.execute(query)
            result = cur.fetchone();
            row["ActorID"] = int(result['PersonID']);
            query = "INSERT INTO ACTOR(ActorID,AvgPayCheck) VALUES('%d','%d')" %(row["ActorID"],c)
            cur.execute(query)
            con.commit()
            print("Inserted into Actor table")
        elif row["Profession"] == 'DIRECTOR':
            query = "SELECT PersonID FROM MAJOR_PERSONALITIES ORDER BY PersonID DESC LIMIT 1"
            cur.execute(query)
            result = cur.fetchone();
            row["DirectorID"] = int(result['PersonID']);
            query = "INSERT INTO DIRECTOR(DirectorID,FavouriteGenre) VALUES('%d','%s')" %(row["DirectorID"],c)
            cur.execute(query)
            con.commit()
            print("Inserted into Director table")
        elif row["Profession"] == 'PRODUCER':
            query = "SELECT PersonID FROM MAJOR_PERSONALITIES ORDER BY PersonID DESC LIMIT 1"
            cur.execute(query)
            result = cur.fetchone();
            row["ProducerID"] = int(result['PersonID']);
            query = "INSERT INTO PRODUCER(ProducerID,AvgBudget) VALUES('%d','%d')" %(row["ProducerID"],c)
            cur.execute(query)
            con.commit()
            print("Inserted into Producer table")
    except:
        con.rollback()
        print("Failed")


def addproduction():
    try:
        row={}
        print("Enter new Production House details: ")
        row["ProductionHouseName"] = input("Name : ")
        row["Founder"] = input("Founder: ")
        sql = "SELECT * FROM INDUSTRY"
        cur.execute(sql)
        result = cur.fetchall();
        temp=[]
        for i in range(0,len(result)):
            print(result[i]['IndustryID'],end=" ")
            print(result[i]['IndustryName'])
            temp.append(result[i]['IndustryID'])
        

        row["IndustryID"] = int(input("Select IndustryID from List : "))
        # error handling
        if row["IndustryID"] in temp:
            query = "INSERT INTO PRODUCTION_HOUSE(ProductionHouseName,Founder,IndustryID) VALUES('%s', '%s', '%d')" %(row["ProductionHouseName"], row["Founder"], row["IndustryID"])
            cur.execute(query)
            con.commit()
            print("Inserted Into Production_House table")
        else:
            print("Industry ID INVALID")
    except Exception as e:
        con.rollback()
        print("Failed")


def delete_in_theatre():
    try:
        sql = "SELECT MovieID,Name from MOVIES where MovieID IN (SELECT MovieID FROM IN_THEATRE)"
        cur.execute(sql)
        result = cur.fetchall();
        temp=[]
        for i in range(0,len(result)):
            print(result[i]['MovieID'],end=" ")
            print(result[i]['Name'])
            temp.append(result[i]['MovieID'])
        w1=input("Select movie id to remove: ")
        
        # error handling
        if int(w1) in temp:

            sql="DELETE FROM IN_THEATRE WHERE MovieID="+w1 
            cur.execute(sql)
            con.commit()
            print("Deleted from IN_THEATRE table")
        else:
            print("MovieID Invalid")
    except Exception as e:
        con.rollback()
        print("Failed")


def update():
    try:
        sql = "SELECT MovieID,Name from MOVIES"
        cur.execute(sql)
        result = cur.fetchall();
        temp1=[]
        for i in range(0,len(result)):
            print(result[i]['MovieID'],end=" ")
            print(result[i]['Name'])
            temp1.append(result[i]['MovieID'])

        w1=input("Select movie id to update: ")
        
        # error handling
        
        if int(w1) in temp1:
            sql= "SELECT * FROM BOX_OFFICE_COLLECTION WHERE MovieID="+w1 
            cur.execute(sql)
            result = cur.fetchall();
            temp2=[]
            for i in range(0,len(result)):
                print(result[i]['MovieID'],end=" ")
                print(result[i]['Country'],end=" ")
                print(result[i]['Collection'])
                temp2.append(result[i]['Country'])

            w2 = input("Select Country to update it's Collection: ")
            if w2 in temp2:
                w3 = input("Write it's new Total Collection: ")
                sql = "UPDATE BOX_OFFICE_COLLECTION SET Collection="+w3+" WHERE MovieID="+w1+" and Country='"+w2+"'"
                cur.execute(sql)
                con.commit()
                
                sql= "SELECT * FROM BOX_OFFICE_COLLECTION WHERE MovieID="+w1 
                cur.execute(sql)
                result = cur.fetchall();
                u=0
                for i in range(0,len(result)):
                    u = int(u) + int(result[i]['Collection'])
                u=str(u)
                sql = "UPDATE MOVIES SET BoxOffice="+u+" WHERE MovieID="+w1
                cur.execute(sql)
                con.commit()
                print("Collection Updated")
            else:
                print("invaild country")
        else:
            print("invalid movieid")

    except Exception as e:
        con.rollback()
        print("Failed")       


def update2():
    try:
        sql = "SELECT MovieID,Name from MOVIES"
        cur.execute(sql)
        result = cur.fetchall();
        temp1=[]
        for i in range(0,len(result)):
            print(result[i]['MovieID'],end=" ")
            print(result[i]['Name'])
            temp1.append(result[i]['MovieID'])
        w1=input("Select movie id to update: ")

        if int(w1) in temp1:

            sql= "SELECT GivenBy,AvgRating FROM RATING_OF_MOVIE WHERE MovieID="+w1 
            cur.execute(sql)
            result = cur.fetchall();
            temp2=[]
            for i in range(0,len(result)):
                print(result[i]['GivenBy'],end=" ")
                print(result[i]['AvgRating'])
                temp2.append(result[i]['GivenBy'])
            w2 = input("Select Name of Rating Platform to update it's Rating: ")
            if w2 in temp2:
                w3 = input("Write it's new Rating: ")
                sql = "UPDATE RATING_OF_MOVIE SET AvgRating="+w3+" WHERE MovieID="+w1+" and GivenBy='"+w2+"'"
                cur.execute(sql)
                con.commit()

                sql= "SELECT * FROM RATING_OF_MOVIE WHERE MovieID="+w1 
                cur.execute(sql)
                result = cur.fetchall();
                u=0
                for i in range(0,len(result)):
                    u = int(u) + int(result[i]['AvgRating'])
                u=int(u/len(result))
                u=str(u)
                sql = "UPDATE MOVIES SET Rating="+u+" WHERE MovieID="+w1
                cur.execute(sql)
                con.commit()
                print("Rating Updated")
            else:
                print("invalid rating Platform")
        else:
            print("movieID invalid")
    except Exception as e:
        con.rollback()
        print("Failed")


def addmovie():
    try:
        # Takes movie details as input
        row = {}
        r1={}
        r2={}
        r3={}
        r4={}
        print("Enter new Movie details: ")
        row["Name"] = input("Name : ")
        row["ReleaseDate"] = input("Release Date (YYYY-MM-DD): ")
        row["RunTime"] = input("RunTime (HH:MM:SS): ")
        row["Genre"] = input("Genre : ")
        row["Budget"] = int(input("Budget (in Cr INR): "))
        sql = "SELECT ProductionHouseID,ProductionHouseName FROM PRODUCTION_HOUSE"
        cur.execute(sql)
        result = cur.fetchall()
        temp1=[]
        for i in range(0,len(result)):
            print(result[i]['ProductionHouseID'],end=" ")
            print(result[i]['ProductionHouseName'])
            temp1.append(result[i]['ProductionHouseID'])
        row["ProductionHouseID"] = int(input("ProductionHouseID : "))
        if row["ProductionHouseID"] not in temp1:
            print("invalid ProductionHouseID")
            return
        b=str(row["ProductionHouseID"])
        sql = "SELECT IndustryID FROM PRODUCTION_HOUSE WHERE ProductionHouseID="+b
        cur.execute(sql)
        result = cur.fetchone()
        row["IndustryID"] = int(result['IndustryID'])
        row["BoxOffice"] = 0;
        row["Rating"] = 0;
        
        var = int(input("enter number of Countries: "))
        u=0
        for x in range(var):
            r1[x] = input("Enter Country Name: ")
            r2[x] = int(input("Enter Collection: "))
            u = int(u) + int(r2[x])
        row["BoxOffice"]=int(u)
        u=0
        var1 = int(input("Enter number of Rating Platforms: "))
        for x in range(var1):
            r3[x] = input("Enter name of rating Platform: ")
            r4[x] = int(input("Enter rating(out of 10): "))
            u = int(u) + int(r4[x])
        row["Rating"] = int(u/var1);

        var2 = int(input("If in Theatre Type 1 else 0: "))
        
        query = "INSERT INTO MOVIES(Name,ReleaseDate,RunTime,Genre,Budget,IndustryID,ProductionHouseID,BoxOffice,Rating) VALUES('%s', '%s', '%s', '%s', '%d', '%d', '%d', '%d', '%d')" %(row["Name"], row["ReleaseDate"], row["RunTime"], row["Genre"], row["Budget"], row["IndustryID"], row["ProductionHouseID"], row["BoxOffice"], row["Rating"])
        cur.execute(query)
        con.commit()
        print("Inserted Into Movie table")

        
        query = "SELECT MovieID FROM MOVIES ORDER BY MovieID DESC LIMIT 1"
        cur.execute(query)
        result = cur.fetchone();
        row["MovieID"] = int(result['MovieID']);

        if var2==1:
           # print(date.today())
            rdate=datetime.strptime( row["ReleaseDate"] , '%Y-%m-%d' ).date()
         #   print(rdate)
            DaysInTheatre = date.today() - rdate
          #  print(DaysInTheatre.days)
            query = "INSERT INTO IN_THEATRE(MovieID,DaysInTheatre) VALUES ('%d', '%s')" %(row["MovieID"], DaysInTheatre.days)
            cur.execute(query)
            con.commit()
            print("Inserted Collection Into IN_THEATRE Database")

        for x in range(var):
            query = "INSERT INTO BOX_OFFICE_COLLECTION(MovieID,Country,Collection) VALUES('%d', '%s', '%d')" %(row["MovieID"], r1[x], r2[x])
            cur.execute(query)
            con.commit()
            print("Inserted Collection Into BOX_OFFICE_COLLECTION Database")    

        for x in range(var1):
            query = "INSERT INTO RATING_OF_MOVIE(MovieID,GivenBy,AvgRating) VALUES('%d', '%s', '%d')" %(row["MovieID"], r3[x], r4[x])
            cur.execute(query)
            con.commit()
            print("Inserted Collection Into RATING_OF_MOVIE Database")    


        Actors = int(input("Enter no of actors: "))
        sql = "SELECT PersonID,PersonName from MAJOR_PERSONALITIES WHERE Profession = 'ACTOR'"
        cur.execute(sql)
        result = cur.fetchall();
        temp3=[]
        for i in range(0,len(result)):
            print(result[i]['PersonID'],end=" ")
            print(result[i]['PersonName'])
            temp3.append(result[i]['PersonID'])

        ActorID = (input("Select Actor ID above options :")).split(' ')

        if Actors != len(ActorID):
            print("Incorrect no of actors")
            return

        for i in range(0,len(ActorID)):
            if int(ActorID[i]) not in temp3:
                print("invalid actor id")
                return

        Producers = int(input("Enter no of producers: "))
        sql = "SELECT PersonID,PersonName from MAJOR_PERSONALITIES WHERE Profession = 'PRODUCER'"
        cur.execute(sql)
        result = cur.fetchall();
        temp4=[]
        for i in range(0,len(result)):
            print(result[i]['PersonID'],end=" ")
            print(result[i]['PersonName'])
            temp4.append(result[i]['PersonID'])

        ProducerID = (input("Select Producer ID above options :")).split(' ')

        if Producers != len(ProducerID):
            print("Incorrect no of producers")
            return

        for i in range(0,len(ProducerID)):
            if int(ProducerID[i]) not in temp4:
                print("invalid producer id")
                return

        sql = "SELECT PersonID,PersonName from MAJOR_PERSONALITIES WHERE Profession = 'DIRECTOR'"
        cur.execute(sql)
        result = cur.fetchall();
        temp5=[]
        for i in range(0,len(result)):
            print(result[i]['PersonID'],end=" ")
            print(result[i]['PersonName'])
            temp5.append(result[i]['PersonID'])

        DirectorID= input("Select Director ID: ")


        for i in range(0,len(temp5)):
            if int(DirectorID) not in temp5:
                print("invalid director  id")
                return

        row["DirectorID"]=int(DirectorID)
        for x in range(Producers):
            row["ProducerID"]=int(ProducerID[x])
            for y in range(Actors):
                row["ActorID"]=int(ActorID[y])
                query = "INSERT INTO ACTED_PRODUCED_DIRECTED(MovieID,DirectorID,ProducerID,ActorID) VALUES ('%d','%d','%d','%d')" %(row["MovieID"],row["DirectorID"],row["ProducerID"],row["ActorID"])
                #print(query)
                cur.execute(query)
                con.commit()
                print("Inserted Into ACTED_PRODUCED_DIRECTED Database")        
    except Exception as e:
        con.rollback()
        print("Failed")

def movieRecommendation():
    try:
        take={}
        print("Min rating of movie you need:")
        take["minRating"]=input()
        print("Min BoxOfficeCollection of movie you need:")
        take["minBoxOffice"]=input()
        actors="SELECT PersonID,PersonName FROM MAJOR_PERSONALITIES WHERE Profession='ACTOR'"
        cur.execute(actors)
        actors_ans=cur.fetchall();
        producers="SELECT PersonID,PersonName FROM MAJOR_PERSONALITIES WHERE Profession='PRODUCER'"
        cur.execute(producers)
        producers_ans=cur.fetchall();
        directors="SELECT PersonID,PersonName FROM MAJOR_PERSONALITIES WHERE Profession='DIRECTOR'"
        cur.execute(directors)
        directors_ans=cur.fetchall();
        for i in range(0,len(actors_ans)):
            print(actors_ans[i]['PersonID'],end=" ")
            print(actors_ans[i]['PersonName'])
        print("Choose an Actor which you want: ")
        actor_want=input()
        for i in range(0,len(producers_ans)):
            print(producers_ans[i]['PersonID'],end=" ")
            print(producers_ans[i]['PersonName'])
        print("Choose an Producer which you want: ")
        producer_want=input()
        for i in range(0,len(directors_ans)):
            print(directors_ans[i]['PersonID'],end=" ")
            print(directors_ans[i]['PersonName'])
        print("Choose an Director which you want: ")
        director_want=input()

        query = "SELECT MovieID FROM MOVIES WHERE Rating>"+take["minRating"]
        cur.execute(query)
        result_rating = cur.fetchall();
        for i in range(0,len(result_rating)):
            result_rating[i]=result_rating[i]['MovieID']


        query = "SELECT MovieID FROM MOVIES WHERE BoxOffice>"+take["minBoxOffice"]
        cur.execute(query)
        result_box_office = cur.fetchall();
        for i in range(0,len(result_box_office)):
            result_box_office[i]=result_box_office[i]['MovieID']

        query="SELECT DISTINCT MovieID FROM ACTED_PRODUCED_DIRECTED WHERE ActorID="+actor_want
        cur.execute(query)
        result_actor = cur.fetchall();
        for i in range(0,len(result_actor)):
            result_actor[i]=result_actor[i]['MovieID']

        query="SELECT DISTINCT MovieID FROM ACTED_PRODUCED_DIRECTED WHERE ProducerID="+producer_want
        cur.execute(query)
        result_producer = cur.fetchall();
        for i in range(0,len(result_producer)):
            result_producer[i]=result_producer[i]['MovieID']

        query="SELECT DISTINCT MovieID FROM ACTED_PRODUCED_DIRECTED WHERE DirectorID="+director_want
        cur.execute(query)
        result_director = cur.fetchall();
        for i in range(0,len(result_director)):
            result_director[i]=result_director[i]['MovieID']
        
        # print(result_rating)
        # print(result_box_office)
        # print(result_actor)
        # print(result_producer)
        # print(result_director)

        query="SELECT COUNT(*) FROM MOVIES"
        cur.execute(query)
        result=cur.fetchone();
        result=result["COUNT(*)"]
        result_all=[]
        result_one=[]
        for i in range(1,result+1):
            if (i in result_actor) and (i in result_director) and (i in result_producer) and (i in result_box_office) and (i in result_rating):
                result_all.append(i)
            if (i in result_actor) or (i in result_director) or (i in result_producer) or (i in result_box_office) or (i in result_rating):
                result_one.append(i)

        print("*************************************************************")
        print("      ***********************************************        ")
        print()
        if len(result_all) > 0:

            print("MOVIES WITH ALL THINGS MATCHING")
            query="SELECT Name FROM MOVIES WHERE MovieID in ("
            for i in range(0,len(result_all)):
                if i != 0:
                    query+=","
                query+=str(result_all[i])
            query+=")"
            # print(query)
            cur.execute(query)
            two=cur.fetchall();
            for i in range(0,len(two)):
                print(two[i]['Name'])
            print()
            print()

        if len(result_one) > 0:
            print("MOVIES WITH ATLEAST ONE MATCHING CRITERIA")
            query="SELECT Name FROM MOVIES WHERE MovieID in ("
            for i in range(0,len(result_one)):
                if i != 0:
                    query+=","
                query+=str(result_one[i])
            query+=")"
            # print(query)
            cur.execute(query)
            one=cur.fetchall();
            for i in range(0,len(one)):
                print(one[i]['Name'])
            print()
            print()
        if len(result_actor) > 0:

            print("MOVIES WITH ACTOR MATCHING ")
            query="SELECT Name FROM MOVIES WHERE MovieID in ("
            for i in range(0,len(result_actor)):
                if i != 0:
                    query+=","
                query+=str(result_actor[i])
            query+=")"
            # print(query)
            cur.execute(query)
            three=cur.fetchall();
            for i in range(0,len(three)):
                print(three[i]['Name'])
            print()
            print()
        if len(result_director)>0:

            print("MOVIES WITH DIRECTOR MATCHING")
            query="SELECT Name FROM MOVIES WHERE MovieID in ("
            for i in range(0,len(result_director)):
                if i != 0:
                    query+=","
                query+=str(result_director[i])
            query+=")"
            # print(query)
            cur.execute(query)
            four=cur.fetchall();
            for i in range(0,len(four)):
                print(four[i]['Name'])
            print()
        print("      ***********************************************        ")
        print("*************************************************************")


    except Exception as e:
        con.rollback()
        print("Failed")


def actorStatistics():
    try:
        actors="SELECT PersonID,PersonName FROM MAJOR_PERSONALITIES WHERE Profession='ACTOR'"
        cur.execute(actors)
        actors_ans=cur.fetchall();
        for i in range(0,len(actors_ans)):
            print(actors_ans[i]['PersonID'],end=" ")
            print(actors_ans[i]['PersonName'])
        print("Choose an Actor whose Stats you want: ")
        actor=input()

        query="SELECT PersonName FROM MAJOR_PERSONALITIES WHERE PersonID="+str(actor)
        cur.execute(query)
        actor_name = cur.fetchone();
        actor_name=actor_name['PersonName']

        query="SELECT DISTINCT MovieID FROM ACTED_PRODUCED_DIRECTED WHERE ActorID="+actor
        cur.execute(query)
        actor_movie = cur.fetchall();


        print("*************************************************************")
        print("      ***********************************************        ")

        if len(actor_movie)>0:
            num="("
            for i in range(0,len(actor_movie)):
                if i != 0:
                    num+=","
                num+=str(actor_movie[i]['MovieID'])
            num+=")"

            query="SELECT count(MovieID) FROM MOVIES WHERE  Rating <=5 and MovieID in "+num
            cur.execute(query)
            numless5 = cur.fetchall();
            numless5=numless5[0]['count(MovieID)']

            query="SELECT count(MovieID) FROM MOVIES WHERE  Rating >5 and Rating<8 and MovieID in "+num
            cur.execute(query)
            numbetween58 = cur.fetchall();
            numbetween58=numbetween58[0]['count(MovieID)']

            query="SELECT count(MovieID) FROM MOVIES WHERE  Rating>=8 and MovieID in "+num
            cur.execute(query)
            numgreater8 = cur.fetchall();
            numgreater8=numgreater8[0]['count(MovieID)']

            query="SELECT count(MovieID) FROM MOVIES WHERE  BoxOffice <=50 and MovieID in "+num
            cur.execute(query)
            numless50 = cur.fetchall();
            numless50=numless50[0]['count(MovieID)']

            query="SELECT count(MovieID) FROM MOVIES WHERE  BoxOffice >50 and BoxOffice <100 and MovieID in "+num
            cur.execute(query)
            numbetween50100 = cur.fetchall();
            numbetween50100=numbetween50100[0]['count(MovieID)']

            query="SELECT count(MovieID) FROM MOVIES WHERE  BoxOffice >=100 and MovieID in "+num
            cur.execute(query)
            numgreater100 = cur.fetchall();
            numgreater100=numgreater100[0]['count(MovieID)']


            query="SELECT ProductionHouseID FROM MOVIES WHERE  MovieID in "+num+" GROUP BY ProductionHouseID ORDER BY COUNT(MovieID) DESC"
            cur.execute(query)
            numhouse = cur.fetchone();
            numhouse=numhouse['ProductionHouseID']

            query="SELECT ProductionHouseName FROM PRODUCTION_HOUSE WHERE ProductionHouseID="+str(numhouse)
            cur.execute(query)
            numhouse = cur.fetchone();
            numhouse=numhouse['ProductionHouseName']

            query="SELECT IndustryID FROM MOVIES WHERE  MovieID in "+num+" GROUP BY IndustryID ORDER BY COUNT(MovieID) DESC"
            cur.execute(query)
            numindustry = cur.fetchone();
            numindustry=numindustry['IndustryID']

            query="SELECT IndustryName FROM INDUSTRY WHERE IndustryID="+str(numindustry)
            cur.execute(query)
            numindustry = cur.fetchone();
            numindustry=numindustry['IndustryName']

            print("ACTOR NAME: " , end=" ")
            print(actor_name)
            print()
            print("Number of Movies Rating less than five:               ", end =" ")
            print(numless5)
            print()
            print("Number of Movies Rating between five and eight:       ", end =" ")
            print(numbetween58)
            print()
            print("Number of Movies Rating greater than eight:           ", end =" ")
            print(numgreater8)
            print()
            print("Number of Movies BoxOffice less than 50:              ", end =" ")
            print(numless50)
            print()
            print("Number of Movies BoxOffice between 50 and 100:        ", end =" ")
            print(numbetween50100)
            print()
            print("Number of Movies BoxOffice greater than 100:          ", end =" ")
            print(numgreater100)
            print()
            print("Production house with which Actor has worked the most:", end =" ")
            print(numhouse)
            print()
            print("Industry in which Actor has worked the most:          ", end =" ")
            print(numindustry)
            print()

        print("      ***********************************************        ")
        print("*************************************************************")

    except Exception as e:
        con.rollback()
        print("Failed")

def directorStatistics():
    try:
        directors="SELECT PersonID,PersonName FROM MAJOR_PERSONALITIES WHERE Profession='DIRECTOR'"
        cur.execute(directors)
        directors_ans=cur.fetchall();
        for i in range(0,len(directors_ans)):
            print(directors_ans[i]['PersonID'],end=" ")
            print(directors_ans[i]['PersonName'])
        print("Choose a Director whose Stats you want: ")
        director=input()
        query="SELECT PersonName FROM MAJOR_PERSONALITIES WHERE PersonID="+str(director)
        cur.execute(query)
        director_name = cur.fetchone();
        director_name=director_name['PersonName']

        query="SELECT DISTINCT MovieID FROM ACTED_PRODUCED_DIRECTED WHERE DirectorID="+director
        cur.execute(query)
        director_movie = cur.fetchall();


        print("*************************************************************")
        print("      ***********************************************        ")

        if len(director_movie)>0:
            num="("
            for i in range(0,len(director_movie)):
                if i != 0:
                    num+=","
                num+=str(director_movie[i]['MovieID'])
            num+=")"
            query="SELECT count(MovieID) FROM MOVIES WHERE  Rating <=5 and MovieID in "+num
            cur.execute(query)
            numless5 = cur.fetchall();
            numless5=numless5[0]['count(MovieID)']

            query="SELECT count(MovieID) FROM MOVIES WHERE  Rating >5 and Rating<8 and MovieID in "+num
            cur.execute(query)
            numbetween58 = cur.fetchall();
            numbetween58=numbetween58[0]['count(MovieID)']

            query="SELECT count(MovieID) FROM MOVIES WHERE  Rating>=8 and MovieID in "+num
            cur.execute(query)
            numgreater8 = cur.fetchall();
            numgreater8=numgreater8[0]['count(MovieID)']

            query="SELECT count(MovieID) FROM MOVIES WHERE  BoxOffice <=50 and MovieID in "+num
            cur.execute(query)
            numless50 = cur.fetchall();
            numless50=numless50[0]['count(MovieID)']

            query="SELECT count(MovieID) FROM MOVIES WHERE  BoxOffice >50 and BoxOffice <100 and MovieID in "+num
            cur.execute(query)
            numbetween50100 = cur.fetchall();
            numbetween50100=numbetween50100[0]['count(MovieID)']

            query="SELECT count(MovieID) FROM MOVIES WHERE  BoxOffice >=100 and MovieID in "+num
            cur.execute(query)
            numgreater100 = cur.fetchall();
            numgreater100=numgreater100[0]['count(MovieID)']


            query="SELECT ProductionHouseID FROM MOVIES WHERE  MovieID in "+num+" GROUP BY ProductionHouseID ORDER BY COUNT(MovieID) DESC"
            cur.execute(query)
            numhouse = cur.fetchone();
            numhouse=numhouse['ProductionHouseID']

            query="SELECT ProductionHouseName FROM PRODUCTION_HOUSE WHERE ProductionHouseID="+str(numhouse)
            cur.execute(query)
            numhouse = cur.fetchone();
            numhouse=numhouse['ProductionHouseName']

            query="SELECT IndustryID FROM MOVIES WHERE  MovieID in "+num+" GROUP BY IndustryID ORDER BY COUNT(MovieID) DESC"
            cur.execute(query)
            numindustry = cur.fetchone();
            numindustry=numindustry['IndustryID']

            query="SELECT IndustryName FROM INDUSTRY WHERE IndustryID="+str(numindustry)
            cur.execute(query)
            numindustry = cur.fetchone();
            numindustry=numindustry['IndustryName']

            print("DIRECTOR NAME: " , end=" ")
            print(director_name)
            print()
            print("Number of Movies Rating less than five:               ", end =" ")
            print(numless5)
            print()
            print("Number of Movies Rating between five and eight:       ", end =" ")
            print(numbetween58)
            print()
            print("Number of Movies Rating greater than eight:           ", end =" ")
            print(numgreater8)
            print()
            print("Number of Movies BoxOffice less than 50:              ", end =" ")
            print(numless50)
            print()
            print("Number of Movies BoxOffice between 50 and 100:        ", end =" ")
            print(numbetween50100)
            print()
            print("Number of Movies BoxOffice greater than 100:          ", end =" ")
            print(numgreater100)
            print()
            print("Production house with which Actor has worked the most:", end =" ")
            print(numhouse)
            print()
            print("Industry in which Actor has worked the most:          ", end =" ")
            print(numindustry)
            print()

        print("      ***********************************************        ")
        print("*************************************************************")

    except Exception as e:
        con.rollback()
        print("Failed")

def dispatch(ch):
    """
    Function that maps helper functions to option entered
    """
    if(ch==1): 
        addmovie()
    elif ch==2:
        addperson()
    elif ch==3:
        delete_in_theatre()
    elif ch==4:
        update()
    elif ch==5:
        update2()
    elif ch==6:
        addproduction()
    elif(ch==7):
        movieRecommendation()
    elif(ch==8):
        actorStatistics()
    elif(ch==9):
        directorStatistics()
    else:
        print("Error: Invalid Option")

# Global
while(1):
    tmp = sp.call('clear',shell=True)
    username = input("Username: ")
    password = input("Password: ")

    try:
        con = pymysql.connect(host='localhost',
                user=username,
                password=password,
                db='BIGSCREEN',
                cursorclass=pymysql.cursors.DictCursor)
        tmp = sp.call('clear',shell=True)

        if(con.open):
            print("Connected")
        else:
            print("Failed to connect")
        tmp = input("Enter any key to CONTINUE>")

        with con:
            cur = con.cursor()
            while(1):
                tmp = sp.call('clear',shell=True)
                print("1. Enter Details about Movie")
                print("2. Add Person")
                print("3. Remove Movie from Theatre")
                print("4. Update Collection")
                print("5. Update Ratings")
                print("6. Add Production")
                print("7. movieRecommendation")
                print("8. actorStatistics")
                print("9. directorStatistics")                
                print("10. Logout")
                ch = int(input("Enter choice> "))
                tmp = sp.call('clear',shell=True)
                if ch==10:
                    break
                else:
                    dispatch(ch)
                    tmp = input("Enter any key to CONTINUE>")
    except:
        tmp = sp.call('clear',shell=True)
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        tmp = input("Enter any key to CONTINUE>")
