PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE countries (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
tld TEXT NOT NULL UNIQUE,
cca2 TEXT NOT NULL UNIQUE,
capital TEXT NOT NULL UNIQUE,
callingCode INTEGER
);
INSERT INTO countries VALUES(21,'Afghanistan','.af','AF','Kabul',93);
INSERT INTO countries VALUES(22,'Italy','.it','IT','Rome',39);
INSERT INTO countries VALUES(23,'Malaysia','.my','MY','Kuala Lumpur',60);
INSERT INTO countries VALUES(24,'Mauritania','.mr','MR','Nouakchott',222);
INSERT INTO countries VALUES(25,'Tunisia','.tn','TN','Tunis',216);
INSERT INTO countries VALUES(26,'Tanzania','.tz','TZ','Dodoma',255);
INSERT INTO countries VALUES(27,'Seychelles','.sc','SC','Victoria',248);
INSERT INTO countries VALUES(28,'Norway','.no','NO','Oslo',47);
INSERT INTO countries VALUES(29,'Nepal','.np','NP','Kathmandu',977);
INSERT INTO countries VALUES(30,'Colombia','.co','CO','Bogota',57);
INSERT INTO countries VALUES(31,'Peru','.pe','PE','Lima',456);
DELETE FROM sqlite_sequence;
INSERT INTO sqlite_sequence VALUES('countries',31);
CREATE INDEX country_id ON countries (id);
COMMIT;
 21|Afghanistan|.af|AF|Kabul|93
22|Italy|.it|IT|Rome|39
23|Malaysia|.my|MY|Kuala Lumpur|60
24|Mauritania|.mr|MR|Nouakchott|222
25|Tunisia|.tn|TN|Tunis|216
26|Tanzania|.tz|TZ|Dodoma|255
27|Seychelles|.sc|SC|Victoria|248
28|Norway|.no|NO|Oslo|47
29|Nepal|.np|NP|Kathmandu|977
30|Colombia|.co|CO|Bogota|57
31|Peru|.pe|PE|Lima|456
database page size:  4096
write format:        1
read format:         1
reserved bytes:      0
file change counter: 120
database page count: 7
freelist page count: 0
schema cookie:       25
schema format:       4
default cache size:  0
autovacuum top root: 0
incremental vacuum:  0
text encoding:       1 (utf8)
user version:        0
application id:      0
software version:    3032003
number of tables:    2
number of indexes:   4
number of triggers:  0
number of views:     0
schema size:         266
data version         3
CREATE TABLE countries (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
tld TEXT NOT NULL UNIQUE,
cca2 TEXT NOT NULL UNIQUE,
capital TEXT NOT NULL UNIQUE,
callingCode INTEGER
);
CREATE INDEX country_id ON countries (id);
21|Afghanistan|.af|AF|Kabul|93
22|Italy|.it|IT|Rome|39
23|Malaysia|.my|MY|Kuala Lumpur|60
24|Mauritania|.mr|MR|Nouakchott|222
25|Tunisia|.tn|TN|Tunis|216
26|Tanzania|.tz|TZ|Dodoma|255
27|Seychelles|.sc|SC|Victoria|248
28|Norway|.no|NO|Oslo|47
29|Nepal|.np|NP|Kathmandu|977
30|Colombia|.co|CO|Bogota|57
31|Peru|.pe|PE|Lima|456
