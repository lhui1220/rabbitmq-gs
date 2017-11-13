FROM rabbitmq:3.6.14

MAINTAINER liuhui

RUN apt-get update

RUN apt-get install -y wget

# donwload plugin
RUN wget -O /usr/lib/rabbitmq/lib/rabbitmq_server-3.6.14/plugins/rabbitmq_delayed_message_exchange-0.0.1.ez  https://bintray.com/rabbitmq/community-plugins/download_file?file_path=rabbitmq_delayed_message_exchange-0.0.1.ez

#enable plugin
RUN rabbitmq-plugins enable rabbitmq_delayed_message_exchange
