source env.rc
#JAVA=/usr/lib/jvm/jre-15-openjdk/bin/java
JAVA=java
JAR=target/restmysqlmodel-1.0-SNAPSHOT-jar-with-dependencies.jar
$JAVA -cp $JAR:$JDBC RestMain -c $PROP -p $PORT