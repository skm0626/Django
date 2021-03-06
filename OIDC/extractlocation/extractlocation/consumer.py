# -*- coding: utf-8 -*-
'''
기능
1) 토픽별로 KafkaConsumer_ 객체(Consumer Group) 생성
'''
from encodings import utf_8
from ensurepip import bootstrap
from select import KQ_FILTER_AIO
from kafka import KafkaConsumer
from kafka import TopicPartition
from pprint import pprint
import json
from collections import OrderedDict
import time
from ast import literal_eval


class KafkaConsumer_:
    def __init__(self):
        self.host = 'localhost:9092'
        self.topic_name = ''
        self.group_id = ''
        self.consumer = KafkaConsumer()
        self.partitions = set()

    def set_consumer(self):
        self.consumer = KafkaConsumer(
            self.topic_name,
            bootstrap_servers=[self.host],
            group_id=self.group_id,
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            value_deserializer=lambda x: x.decode('utf-8'),
            consumer_timeout_ms=100000,
        )

    def set_group_id(self,group_id):
        self.group_id=group_id

    def get_group_id(self):
        return self.group_id

    def set_host(self,host):
        self.host = host

    def get_host(self):
        return self.host

    def set_topic_name(self,topic_name):
        self.topic_name = topic_name

    def get_topic_name(self):
        return self.topic_name

    def get_partitions(self):
        partitions=self.consumer.partitions_for_topic(self.topic_name)
        return partitions

    def ear_consumer(self):
        print('[begin] get consumer list')
        for message in self.consumer:
            print("Topic: %s, Partition: %d, Offset: %d, Key: %s, Value: %s" \
            % ( message.topic, message.partition, message.offset, message.key, message.value ))
        print('[end] get consumer list')


    def _consume(self):
        partitions = self.get_partitions()
        print(partitions)
        # 파티션 별 last offset 읽기
        for p_id in partitions:
            print ('offset '+str(p_id)+' before = '+str(self.consumer.committed(TopicPartition(self.topic_name, p_id))))

        # 파티션0 현재 offset num 저장
        p0_offset_before= self.consumer.committed(TopicPartition(self.topic_name,0))
        # 시간 측정
        start=time.time()

        # 한번 연결하고 계속 데이터를 가지고 올 것이기 때문에 무한루프로 실행
        while True :
            # last offset 기준으로 record 컨슘하기 - poll()
            msg_pack = self.consumer.poll(timeout_ms=500)
            self.consumer.commit()
            # 파티션0 현재 offset num 저장
            p0_offset_after = self.consumer.committed(TopicPartition(self.topic_name,0))
            print(p0_offset_after,type(p0_offset_after))

            # 새로 들어온 데이터가 특정 개수 이상이면 json파일을 열어 데이터를 적재합니다.
            # if p0_offset_after - p0_offset_before > 10 :
                # print(111111)
            with open('./json_files/test.json','w',encoding='utf-8') as f:
                p0_offset_before=p0_offset_after
                for tp, messages in msg_pack.items():
                    for message in messages:
                        data=literal_eval(message.value)
                        print(data)
                        print(type(data)) # dict 형태
                        json.dump(data,f,ensure_ascii=False)
                        f.write('\n')

            # 5초 주기로 new record 확인
            time.sleep(5)

# removing emoji
def rmEmoji_ascii(inputString):
    return inputString.encode('utf-8', 'ignore').decode('utf-8')


if __name__ == '__main__':
    consumer = KafkaConsumer( 'youplace-part', bootstrap_servers=['localhost:9092'], auto_offset_reset='earliest', enable_auto_commit=True, group_id='my-group', value_deserializer=lambda x: x.decode('utf-8'), consumer_timeout_ms=1000 )
    print('[begin] get consumer list')
    count=0

    import re

    with open('./json_files/test.json','w',encoding='utf-8') as f:
        for messages in consumer:
            str_data=messages.value
            data=eval(str_data)
            # print(data)
            # print(type(data))
            data['title']=rmEmoji_ascii(data['title'])
            # print(str(data))
            # str_data=str(data)
            # f.write(str_data)
            json.dump(data,f)
            f.write('\n')
            count+=1
    print(count)
    f.close()

    # consumer = KafkaConsumer_()
    # consumer.set_group_id('youplace-consumer')
    # consumer.set_topic_name('youplace-part')
    # consumer.set_consumer()
    # consumer.ear_consumer()
    # consumer._consume()
