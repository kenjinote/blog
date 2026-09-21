import os
import re

blog_dir = r'c:\work\kenji.blog\content\post'
targets = {
    'rdbms-transaction-acid-isolation-level-lock': [
        "RDBMS", "ACID", "\u30c8\u30e9\u30f3\u30b6\u30af\u30b7\u30e7\u30f3", "Transaction", "Isolation Level", "\u5206\u96e2\u30ec\u30d9\u30eb", "MVCC", "Lock", "\u30ed\u30c3\u30af"
    ],
    'nosql-database-selection-kvs-document-graph-wide-column': [
        "NoSQL", "Key-Value", "KVS", "Document DB", "\u30c9\u30ad\u30e5\u30e1\u30f3\u30c8\u6307\u5411", "Graph DB", "\u30b0\u30e9\u30d5DB", "Wide-Column", "Redis", "MongoDB", "Neo4j", "Cassandra"
    ],
    'microservices-architecture-bff-api-gateway': [
        "Microservices", "Microservice", "\u30de\u30a4\u30af\u30ed\u30b5\u30fc\u30d3\u30b9", "API Gateway", "BFF", "Backend for Frontend"
    ],
    'event-driven-architecture-message-queue-kafka-rabbitmq': [
        "Event-Driven", "\u30a4\u30d9\u30f3\u30c8\u99c6\u52d5", "Message Queue", "\u30e1\u30c3\u30bb\u30fc\u30b8\u30ad\u30e5\u30fc", "Kafka", "RabbitMQ", "Pub/Sub"
    ],
    'cap-theorem-distributed-systems-tradeoff': [
        "CAP\u5b9a\u7406", "CAP Theorem", "Distributed System", "\u5206\u6563\u30b7\u30b9\u30c6\u30e0", "Consistency", "Availability", "Partition Tolerance", "Eventual Consistency", "\u7d50\u679c\u7684\u6574\u5408\u6027"
    ]
}

split_pattern = re.compile(r'(!?\[[^\]]*\]\([^\)]+\)|```.*?```|`[^`]+`)', re.DOTALL)

count = 0
for root, dirs, files in os.walk(blog_dir):
    for file in files:
        if file.endswith('.md'):
            file_path = os.path.join(root, file)
            
            lang_prefix = ""
            parts_file = file.split('.')
            if len(parts_file) == 3 and parts_file[2] == 'md':
                lang_prefix = "/" + parts_file[1]
                
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                parts = content.split('---', 2)
                if len(parts) >= 3:
                    front_matter = '---' + parts[1] + '---'
                    body = parts[2]
                else:
                    front_matter = ''
                    body = content
                
                tokens = split_pattern.split(body)
                changed = False
                
                for target_slug, keywords in targets.items():
                    if target_slug in root:
                        continue
                        
                    for i in range(0, len(tokens)):
                        text = tokens[i]
                        if not text: continue
                        
                        if i % 2 == 0:
                            for kw in keywords:
                                if kw in text:
                                    if kw.isalpha() and len(kw) <= 5:
                                        pattern = r'(?<![a-zA-Z])' + re.escape(kw) + r'(?![a-zA-Z])'
                                        if re.search(pattern, text):
                                            link_str = f"[{kw}](https://kenji.blog{lang_prefix}/p/{target_slug}/)"
                                            text = re.sub(pattern, link_str, text, count=1)
                                            changed = True
                                    else:
                                        link_str = f"[{kw}](https://kenji.blog{lang_prefix}/p/{target_slug}/)"
                                        text = text.replace(kw, link_str, 1)
                                        changed = True
                            tokens[i] = text
                
                if changed:
                    new_body = "".join(tokens)
                    new_content = front_matter + new_body
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    count += 1
            except Exception as e:
                pass

print(f"Updated {count} markdown files for phase 8 links.")
