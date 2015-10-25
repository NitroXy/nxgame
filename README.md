NXGame
===========

How To: Setup
------------
1. git submodule init && git submodule update
1. Skapa en apache-site för nxgame. (rimligtvis lägger du till en adress, typ nx.dev i /etc/hosts). Kom ihåg AllowOverride All
1. Enable mod rewrite i apache
1. Skapa en databas i mysql (nxgame typ)
1. Importera databasdump
1. Kör ./migrations/update_database.php
1. Ändra i config.php för rätt inställningar (event, databas)
1. Lägg manuellt in ett nytt entry i tabellen "game" (todo:inte behöva detta steg)
1. Enjoy!

How To: Installera php (debian)
--------------
1. apt-get install apache2 libapache2-mod-php5 mysql-server php5-mysql php5-curl
1. Laga php: I /etc/php5/apache2/php.ini
	1. display_errors = On (off för produktion såklart)
	1. error_reporting = E_ALL
	1. default_charset = UTF-8
	1. short_open_tag = On
