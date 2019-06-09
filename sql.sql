

CREATE DATABASE `book_db` DEFAULT CHARACTER SET = `utf8mb4`;



DROP TABLE IF EXISTS `user`;
SELECT * FROM admin
DROP TABLE USER ;
CREATE TABLE `admin` (
  `id` BIGINT(20) NOT NULL AUTO_INCREMENT COMMENT '管理员id',
  `nickname` VARCHAR(100) NOT NULL DEFAULT '' COMMENT '管理员姓名',
  `mobile` VARCHAR(20) NOT NULL DEFAULT '' COMMENT '手机号码',
  `email` VARCHAR(100) NOT NULL DEFAULT '' COMMENT '邮箱地址',
  `sex` TINYINT(1) NOT NULL DEFAULT '0' COMMENT '性别 1：男 2：女 0：未填写',
  `avatar` VARCHAR(64) NOT NULL DEFAULT '' COMMENT '头像',
  `login_name` VARCHAR(20) NOT NULL DEFAULT '' COMMENT '登录用户名',
  `login_pwd` VARCHAR(32) NOT NULL DEFAULT '' COMMENT '登录密码',
  `login_salt` VARCHAR(32) NOT NULL DEFAULT '' COMMENT '随机加密秘钥',
  `status` TINYINT(1) NOT NULL DEFAULT '1' COMMENT '1：有效 0：无效',
  `updated_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '最后一次更新时间',
  `created_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '插入时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `login_name` (`login_name`)
) ENGINE=INNODB DEFAULT CHARSET=utf8mb4 COMMENT='管理员表';

INSERT INTO `admin` (`id`, `nickname`, `mobile`, `email`, `sex`, `avatar`, `login_name`, `login_pwd`, `login_salt`, `status`, `updated_time`, `created_time`)
VALUES (1, 'TIM_MIN', '1899996666', 'TIM_MAN@fjut.edu', 1, '', 'TIM_MAN', '816440c40b7a9d55ff9eb7b20760862c', 'cF3JfH5FJfQ8B2Ba', 1, '2019-03-15 14:08:48', '2019-03-15 14:08:48');


DROP TABLE IF EXISTS `app_access_log`;

CREATE TABLE `app_access_log` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `aid` BIGINT(20) NOT NULL DEFAULT '0' COMMENT 'aid',
  `referer_url` VARCHAR(255) NOT NULL DEFAULT '' COMMENT '当前访问的refer',
  `target_url` VARCHAR(255) NOT NULL DEFAULT '' COMMENT '访问的url',
  `query_params` TEXT NOT NULL COMMENT 'get和post参数',
  `ua` VARCHAR(255) NOT NULL DEFAULT '' COMMENT '访问ua',
  `ip` VARCHAR(32) NOT NULL DEFAULT '' COMMENT '访问ip',
  `note` VARCHAR(1000) NOT NULL DEFAULT '' COMMENT 'json格式备注字段',
  `created_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `idx_aid` (`aid`)
) ENGINE=INNODB DEFAULT CHARSET=utf8mb4 COMMENT='管理员访问记录表';


DROP TABLE IF EXISTS `app_error_log`;
CREATE TABLE `app_error_log` (
  `id` INT(11) UNSIGNED NOT NULL AUTO_INCREMENT,
  `referer_url` VARCHAR(255) NOT NULL DEFAULT '' COMMENT '当前访问的refer',
  `target_url` VARCHAR(255) NOT NULL DEFAULT '' COMMENT '访问的url',
  `query_params` TEXT NOT NULL COMMENT 'get和post参数',
  `content` LONGTEXT NOT NULL COMMENT '日志内容',
  `created_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '插入时间',
  PRIMARY KEY (`id`)
) ENGINE=INNODB  DEFAULT CHARSET=utf8mb4 COMMENT='app错误日表';



DROP TABLE IF EXISTS `member`;
SELECT * FROM member 


DROP TABLE IF EXISTS `oauth_member_bind`;
SELECT * FROM member
SELECT * FROM oauth_member_bind
CREATE TABLE `oauth_member`book`_bind` (
  `id` INT(11) UNSIGNED NOT NULL AUTO_INCREMENT,
  `member_id` INT(11) NOT NULL DEFAULT '0' COMMENT '会员id',
  `client_type` VARCHAR(20) NOT NULL DEFAULT '' COMMENT '客户端来源类型。qq,weibo,weixin',
  `type` TINYINT(3) NOT NULL DEFAULT '0' COMMENT '类型 type 1:wechat ',
  `openid` VARCHAR(80) NOT NULL DEFAULT '' COMMENT '第三方id',
  `unionid` VARCHAR(100) NOT NULL DEFAULT '',
  `extra` TEXT NOT NULL COMMENT '额外字段',
  `updated_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '最后更新时间',
  `created_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '插入时间',
  PRIMARY KEY (`id`),
  KEY `idx_type_openid` (`type`,`openid`)
) ENGINE=INNODB DEFAULT CHARSET=utf8mb4 COMMENT='第三方登录绑定关系';



DROP TABLE IF EXISTS `book`;
SELECT * FROM member_address
SELECT * FROM member_comments
SELECT * FROM book
CREATE TABLE `book` (
  `book_id` INT(11) UNSIGNED NOT NULL AUTO_INCREMENT,
  `cat_id` INT(11) NOT NULL DEFAULT '0' COMMENT '分类id',
  `book_isbn13` VARCHAR(13) NOT NULL DEFAULT '0' COMMENT 'isbn13',
  `book_title` VARCHAR(30) NOT NULL DEFAULT '' COMMENT '书籍名称',
  `book_author` VARCHAR(80) NOT NULL DEFAULT '' COMMENT '作者名称',
  `book_price` DECIMAL(10,2) NOT NULL DEFAULT '0.00' COMMENT '售价',
  `book_oprice` DECIMAL(10,2) NOT NULL DEFAULT '0.00' COMMENT '原价',
  `book_main_image` VARCHAR(100) NOT NULL DEFAULT '' COMMENT '主图',
  `book_grade` DOUBLE DEFAULT NULL COMMENT '书籍评分',
  `book_press` VARCHAR(30) NOT NULL DEFAULT '' COMMENT '出版社',
  `book_binding` VARCHAR(10) NOT NULL DEFAULT '' COMMENT '装帧',
  `book_desc` TEXT COMMENT '书籍简介',
  `book_degrees` VARCHAR(10) NOT NULL DEFAULT '' COMMENT '新旧程度',
  `book_stock` INT(11) NOT NULL DEFAULT '0' COMMENT '库存量',
  `tags` VARCHAR(200) NOT NULL DEFAULT '' COMMENT 'tag关键字，以","连接',
  `book_status` TINYINT(1) NOT NULL DEFAULT '1' COMMENT '状态 1：有效 0：无效',
  `book_month_count` INT(11) NOT NULL DEFAULT '0' COMMENT '月销售数量',
  `book_total_count` INT(11) NOT NULL DEFAULT '0' COMMENT '总销售量',
  `book_view_count` INT(11) NOT NULL DEFAULT '0' COMMENT '总浏览次数',
  `book_comment_count` INT(11) NOT NULL DEFAULT '0' COMMENT '总评论量',
  `book_updated_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '最后更新时间',
  `book_created_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '最后插入时间',
  PRIMARY KEY (`book_id`)
) ENGINE=INNODB DEFAULT CHARSET=utf8mb4 COMMENT='书籍表';

INSERT INTO `book` (`cat_id`, `book_isbn13`, `book_title`, `book_author`, `book_price`, `book_oprice`, `book_main_image`, `book_grade`, 
			`book_press`, `book_binding`, `book_desc`, `book_degrees`, `book_stock`, `tags`, `book_status`) 
			VALUES ('1', '9787536692930', '三体', '刘慈欣', '12.00', '23.00', 'https://img1.doubanio.com\\/view\\/subject\\/s\\/public\\/s2768378.jpg','9.9', '重庆出版社', 
			'平装', '文化大革命如火如荼进行的同时。军方探寻外星文明的绝秘计划“红岸工程”取得了突破性进展。但在按下发射键的那一刻，历经劫难的叶文洁没有意识到，她彻底改变了人类的命运。地球文明向宇宙发出的第一声啼鸣，以太阳为中心，以光速向宇宙深处飞驰……\\n四光年外，“三体文明”正苦苦挣扎——三颗无规则运行的太阳主导下的百余次毁灭与重生逼迫他们逃离母星。而恰在此时。他们接收到了地球发来的信息。在运用超技术锁死地球人的基础科学之后。三体人庞大的宇宙舰队开始向地球进发……\\n人类的末日悄然来临。', 
			'1', '5', '科幻', '1')
INSERT INTO `book` (`cat_id`, `book_isbn13`, `book_title`, `book_author`, `book_price`, `book_oprice`, `book_main_image`, `book_grade`, `book_press`, `book_binding`, `book_desc`, `book_degrees`, `book_stock`, `tags`, `book_status`) VALUES( "1","9787533917067","变形记"," [奥] 卡夫卡 ", "16.00" , "16.00" ," https://img3.doubanio.com/view/subject/m/public/s26042134.jpg", "8.4"," 浙江文艺出版社 "," 平装 "," 1 判决 2 变形记 3 司炉 4 在流放营 5 乡村医生 6 饥饿艺术家 7 铁桶骑士 8 万里长城建造时 9 一条狗的研究 10 中国人来访 ……"," 9 "," 39", "卡夫卡 "," 1")
INSERT INTO `book` (`cat_id`, `book_isbn13`, `book_title`, `book_author`, `book_price`, `book_oprice`, `book_main_image`, `book_grade`, `book_press`, `book_binding`, `book_desc`, `book_degrees`, `book_stock`, `tags`, `book_status`) VALUES( "1","9787115308108","具体数学","Ronald L.Graham", "99.00" , "99.00" ," https://img3.doubanio.com/view/subject/m/public/s26372180.jpg", "9.6","人民邮电出版社","平装","本书介绍了计算机的数学基础，内容涉及求和、取整函数、数论、二项式系数、特殊数、母函数（发生函数）、离散概率、渐近等等，面向从事计算机科学、计算数学、计算技术诸方面工作的人员，以及高等院校相关专业的师生。","10","13", "数学","1")
INSERT INTO `book` (`cat_id`, `book_isbn13`, `book_title`, `book_author`, `book_price`, `book_oprice`, `book_main_image`, `book_grade`, `book_press`, `book_binding`, `book_desc`, `book_degrees`, `book_stock`, `tags`, `book_status`) VALUES( "1","9787121106101","编码","[美] Charles Petzold", "55.00" , "55.00" ," https://img3.doubanio.com/view/subject/m/public/s4379914.jpg", "9.2","电子工业出版社","平装","本书讲述的是计算机工作原理。作者用丰富的想象和清晰的笔墨将看似繁杂的理论阐述得通俗易懂，你丝毫不会感到枯燥和生硬。更重要的是，你会因此而获得对计算机工作原理较深刻的理解。这种理解不是抽象层面上的，而是具有一定深度的。","1","41", "计算机","1")
INSERT INTO `book` (`cat_id`, `book_isbn13`, `book_title`, `book_author`, `book_price`, `book_oprice`, `book_main_image`, `book_grade`, `book_press`, `book_binding`, `book_desc`, `book_degrees`, `book_stock`, `tags`, `book_status`) VALUES( "1","9787111321330","深入理解计算机系统（原书第2版）","（美）Randal E.Bryant", "99.00" , "99.00" ," https://img3.doubanio.com/view/subject/m/public/s4510534.jpg", "9.7","机械工业出版社","平装","本书从程序员的视角详细阐述计算机系统的本质概念，并展示这些概念如何实实在在地影响应用程序的正确性、性能和实用性。全书共12章，主要内容包括信息的表示和处理、程序的机器级表示、处理器体系结构、优化程序性能、存储器层次结构、链接、异常控制流、虚拟存储器、系统级I/O、网络编程、并发编程等。书中提供大量的例子和练习，并给出部分答案，有助于读者加深对正文所述概念和知识的理解。 本书的最大优点是为程序员描述计算机系统的实现细节，帮助其在大脑中构造一个层次型的计算机系统，从最底层的数据在内存中的表示到流水线指令的构成，到虚拟存储器，到编译系统，到动态加载库，到最后的用户态应用。通过掌握程序是如何映射到系统上，以及程序是如何执行的，读者能够更好地理解程序的行为为什么是这样的，以及效率低下是如何造成的。 本书适合那些想要写出更快、更可靠程序的程序员阅读，也适合作为高等院校计算机及相关专业本科生、研究生的教材。","3","11", "计算机系统","1")
INSERT INTO `book` (`cat_id`, `book_isbn13`, `book_title`, `book_author`, `book_price`, `book_oprice`, `book_main_image`, `book_grade`, `book_press`, `book_binding`, `book_desc`, `book_degrees`, `book_stock`, `tags`, `book_status`) VALUES( "1","9787302058144","计算机程序设计艺术（第1卷）","[美] Donald E. Knuth", "80.00" , "80.00" ," https://img3.doubanio.com/view/subject/m/public/s9773641.jpg", "9.4","清华大学出版社","精装","第1卷首先介绍编程的基本概念和技术，然后详细讲解信息结构方面的内容，包括信息在计算机内部的表示方法、数据元素之间的结构关系，以及有效的信息处理方法。此外，书中还描述了编程在模拟、数值方法、符号计算、软件与系统设计等方面的初级应用。此第3版增加了数十项简单但重要的算法和技术，并根据当前研究发展趋势在数学预备知识方面做了大量修改。","10","15", "算法","1")
INSERT INTO `book` (`cat_id`, `book_isbn13`, `book_title`, `book_author`, `book_price`, `book_oprice`, `book_main_image`, `book_grade`, `book_press`, `book_binding`, `book_desc`, `book_degrees`, `book_stock`, `tags`, `book_status`) VALUES( "1","9787301150894","经济学原理","[美] N.格里高利·曼昆", "54.00" , "54.00" ," https://img3.doubanio.com/view/subject/m/public/s3802186.jpg", "9.4","北京大学出版社","平装","《经济学原理(第5版):微观经济学分册》是世界上最流行的经济学教材！其英文原版现已被哈佛大学、耶鲁大学、斯坦福大学等美国600余所大学用作经济学原理课程的教材迄今为止它已被翻译成20种语言在全世界销售100多万册！《经济学原理(第5版):微观经济学分册》前四版的中译本自1999年出版以来也一直是国内选用最多、最受欢迎的经济学教材！在继续保持条理清晰、易于理解的写作风格基础上，曼昆教授在第5版中对全书36章都做了精心修订；同时也更新了大部分“新闻摘录”和部分“案例研究”；此外，为帮助教师进行课堂设计和课堂讲解，本版还极大地丰富了教辅资源。","1","30", "经济学","1")
INSERT INTO `book` (`cat_id`, `book_isbn13`, `book_title`, `book_author`, `book_price`, `book_oprice`, `book_main_image`, `book_grade`, `book_press`, `book_binding`, `book_desc`, `book_degrees`, `book_stock`, `tags`, `book_status`) VALUES( "1","9787508685519","薛兆丰经济学讲义","薛兆丰", "98" , "98" ," https://img1.doubanio.com/view/subject/m/public/s29787408.jpg", "8.5","中信出版集团","精装","我们每天收到无数纷繁复杂的信息，看到各种光怪陆离的现象，世界是复杂的。 世界又并不复杂，只是你需要一双慧眼。经济学是一种帮助你成为明白人的智慧，它是观察世界的视角和态度，而不是一堆函数、公式和图表。 薛兆丰老师善于把复杂的现象用简单直接的方式说清楚。这本书讲解了生活中不可能绕过的经济学核心概念，比如稀缺、成本、价格、交易、信息不对称、收入等与个人生活密切相关的知识，通过大量真实案例的经济学分析，更实际、更有趣、更深入和彻底地将经济学思维运用于各种实际场景，帮你绕过经济学花招，理解现象背后的经济逻辑，从而启发你将同样的思维运用到日常生活和工作中去。 你将摆脱直觉和经验的控制，拥有可以举一反三、能够学以致用的知识体系，从而对这个由海量陌生人连接而成的社会做出恰如其分的反应。 相信读完本书之后，你会对自己身处的世界有更深刻的理解，成为这个复杂世界的明白人。","2","25", "经济学","1")
INSERT INTO `book` (`cat_id`, `book_isbn13`, `book_title`, `book_author`, `book_price`, `book_oprice`, `book_main_image`, `book_grade`, `book_press`, `book_binding`, `book_desc`, `book_degrees`, `book_stock`, `tags`, `book_status`) VALUES( "1","9787100023627","有闲阶级论","[美] 凡勃伦", "16.00" , "16.00" ," https://img3.doubanio.com/view/subject/m/public/s28121915.jpg", "8.1","商务印书馆","平装","本书的主旨在于讨论作为现代生活中一个经济因素的有闲阶级的地位和价值，但是要把讨论严格地限制在这样标明的范围以内是办不到的。因此关于制度的起源和演进以及一般不列入经济学范围以内的一些社会生活特征，这里也不得不给以相当的注意。","3","34", "社会学","1")
INSERT INTO `book` (`cat_id`, `book_isbn13`, `book_title`, `book_author`, `book_price`, `book_oprice`, `book_main_image`, `book_grade`, `book_press`, `book_binding`, `book_desc`, `book_degrees`, `book_stock`, `tags`, `book_status`) VALUES( "1","9787020084203","绝望恸哭的信徒","[日] 野村美月 文", "20.00" , "20.00" ," https://img3.doubanio.com/view/subject/m/public/s6287113.jpg", "8.8","人民文学出版社","平装","快要毕业的远子学姐和心叶似乎有些渐行渐远，为此感到寂寞的心叶却并不承认心底的感觉。他继续跟七濑保持着交往，而他们的关系在一起去新年参拜之后，愈来愈近……此时，不知怎地，七濑突然住院！而前往探望的心叶，竟然跟他未曾淡忘的少女井上美羽重逢！那个代表了心叶心底最深的秘密的少女，就这样重新出现在心叶的眼前。 少女的微笑一如往常，可是心叶和周围人们的关系却因她产生剧烈摩擦。到底什么才是真实？她期望的又是什么── 在文学少女的“想象”中，少女真正的想法是—— 让人意想不到的精彩故事，文学少女第五弹！","3","17", "轻小说","1")
INSERT INTO `book` (`cat_id`, `book_isbn13`, `book_title`, `book_author`, `book_price`, `book_oprice`, `book_main_image`, `book_grade`, `book_press`, `book_binding`, `book_desc`, `book_degrees`, `book_stock`, `tags`, `book_status`) VALUES( "1","9787550258402","古典传统","[美]吉尔伯特·海厄特（Gilbert Highet)", "78.00" , "78.00" ," https://img3.doubanio.com/view/subject/m/public/s28278820.jpg", "9.5","北京联合出版公司·后浪出版公司","平装","哈佛、耶鲁、普林斯顿、中国人民大学教授联合推荐 比较文学领域、古典文化接受史领域里程碑式著作 一部紧扣主脉、细节饱满、层次丰富的西方文学史 【推荐】 海厄特的大著是一部地道的欧洲文学史，它当然有助于我们更好地认识欧洲文明，但在我看来，这部出色的著作其实更有助于我们更好地认识中国文明。 ——刘小枫，中国人民大学文学院教授，中山大学“逸仙学者”讲座教授 我希望海厄特的中国读者通过这本著作，让“我们”的文化也“从希腊人那里学会了思想生活的重要性……和唯一不朽的财富：灵魂”。 ——雷立柏，中国人民大学文学院教授 海厄特不太可能把我看做他的天命读者，但在《古典传统》出版六十年后重读本书时，书中在记录古典作品对西方文学之影响时的出色编排和细节仍让我像当年一样钦佩。我与海厄特只有一面之缘，但暮年的我仍然对他的学识和热情心存感激。他的书仍然活着，并将继续活下去。 ——哈罗德·布鲁姆，耶鲁大学斯特林人文学讲座教授 重读海厄特的《古典传统》，我再一次感受到了它的魔力。与库尔提乌斯的《欧洲文学与拉丁语中世纪》一样，本书是古典学在20世纪中叶那个特定时代的一座丰碑，它饱含人文精神，立足保守态度，致力于复原遭遇纳粹暴行后显得分崩离析的西方文明。广博的内容和宏大的概览赋予了其力量。 ——斯蒂芬·格林布拉特，哈佛大学约翰·科根校级特聘人文学讲座教授 自六十多年前海厄特的著作第一次出版后，它仍是希腊罗马文学在后世的全部故事的最佳单卷本指南。《古典传统》充分展现了这段千年历史的复杂性：海厄特不仅描绘了古典著作如何塑造了后世的读者，还告诉了我们中世纪及现代的作者如何利用古典元素创作出自己的独特作品。博学、妙语频出、恪守人文主义，海厄特的著作既全面又好读。 ——安东尼·格拉夫敦，普林斯顿大学亨利·普特南校级特聘历史学讲座教授 【编辑推荐】 ⊙ 本书出版以来60多年间被翻译成多种欧洲语言与日语，早已奠定了学术经典的地位。 ⊙ 本书勾勒了古典传统影响西欧和美国文学的主要途径，范围宽广；重要作家和作品被放在与古典文化的关系下进行检视，具有其他文学史难以企及的深度。 ⊙ 全书语言博雅晓畅，没有当代文学评论的学术黑话，稍具文学史常识即可顺利阅读。 【内容简介】 本书自1949年出版以来，陆续被翻译为多种欧洲语言及日语，是比较文学领域赫拉克勒斯式的壮举，也是古典文化接受史领域的里程碑式著作。 本书的主旨是勾勒希腊语和拉丁语传统影响西欧与美国文学的主要途径。以此为线索，作者带领读者对西方文学进行了全面的考察。全书自古希腊罗马文明的衰亡和日耳曼蛮族文学在“黑暗时代”破土而生写起，描绘了直到20世纪初西方文学的发展脉络，涉及众多的人物与主题。书中谈到了奥维德对法国中世纪文学的影响、乔叟对维吉尔和西塞罗的借鉴、文艺复兴时期基督教文学与“异教”文学对抗、巴洛克时期对塞内卡的模仿及讽刺作品的重生，经过革命时代灿若星河的天才，最终落脚在现代主义的诞生和成型。 全书以博雅晓畅的语言写成，没有现代文学批评中充斥着的学术黑话，作者以轻柔而富有魅力的语调，将贯穿在西方文学传统中的核心主线向读者娓娓道来。这也许不是面面俱到的文学史，却是一部紧扣主脉、细节饱满、层次丰富的立体的文学史。","1","37", "古典学","1")
INSERT INTO `book` (`cat_id`, `book_isbn13`, `book_title`, `book_author`, `book_price`, `book_oprice`, `book_main_image`, `book_grade`, `book_press`, `book_binding`, `book_desc`, `book_degrees`, `book_stock`, `tags`, `book_status`) VALUES( "1","9787543425651","项链","[法] 莫泊桑", "28.00" , "28.00" ," https://img1.doubanio.com/view/subject/m/public/s1240228.jpg", "8.3","河北教育出版社","平装","莫泊桑被尊称为“世界短篇小说之王”，他将短篇小说的趣味提升到前所未有的高度。在他的笔下，各种社会事件，如战争、政变、普选等，都得到了如实的表现；各个阶层的生活，如上层人士的纸醉金迷，中产阶级的锱必较，乡人村姑的朴素自然，都得到了形象的描绘；各种各样的人物，贵族、官僚、职员、店主、乞丐、妓女，都得到了逼真的刻画；各种各样的场景，如豪华的晚会、精致的沙龙、荒蛮的原野、喧哗的集镇、森严的官府、热门的街道，都得到了生动的写照。可以说，莫泊桑的短篇小说，是一幅栩栩如生的19世纪下半叶法国社会风俗长卷。","1","35", "莫泊桑","1")
INSERT INTO `book` (`cat_id`, `book_isbn13`, `book_title`, `book_author`, `book_price`, `book_oprice`, `book_main_image`, `book_grade`, `book_press`, `book_binding`, `book_desc`, `book_degrees`, `book_stock`, `tags`, `book_status`) VALUES( "1","9787530211168","倾城之恋","张爱玲", "29.80" , "29.80" ," https://img3.doubanio.com/view/subject/m/public/s10205753.jpg", "8.7","北京出版集团公司,北京十月文艺出版社","平装","传奇里的倾国倾城的人大抵如此。 到处都是传奇，可不见得有这么圆满的收场。胡琴咿咿哑哑拉着，在万盏灯的夜晚，拉过来又拉过去，说不尽的苍凉的故事——不问也罢！ 白流苏和范柳原这一对现实庸俗的男女，在战争的兵荒马乱之中被命运掷骰子般地掷到了一起，于“一刹那”体会到了“一对平凡的夫妻”之间的“一点真心”。 本书收录张爱玲于一九四三年至一九四四年创作的中短篇小说，包括《第一炉香》《第二炉香》《茉莉香片》《心经》等。","2","6", "张爱玲","1")
INSERT INTO `book` (`cat_id`, `book_isbn13`, `book_title`, `book_author`, `book_price`, `book_oprice`, `book_main_image`, `book_grade`, `book_press`, `book_binding`, `book_desc`, `book_degrees`, `book_stock`, `tags`, `book_status`) VALUES( "1","9787532759064","哈扎尔辞典（阳本）","(塞尔维亚)米洛拉德·帕维奇", "45.00" , "45.00" ," https://img3.doubanio.com/view/subject/m/public/s24590723.jpg", "8.8","上海译文出版社","精装","这是一部关于盗梦和秘密的迷宫辞典体小说，包括一明一暗两条线索：历史线索和魔幻线索。历史线索即作者明确告诉我们的，历史上出现过一次哈扎尔大论辩，目的在于帮助哈扎尔可汗选择宗教。在可汗邀请下，基督教、犹太教和伊斯兰教的代表都汇集到哈扎尔首都，举行了一次大论辩。对于辩论结果，各个宗教都有自己的说法。由于哈扎尔人自己写的历史已淹没无闻，只能通过基督教、犹太教和伊斯兰教的文献来佐证这次大论辩的结果。但三个宗教记载的结果相互矛盾，都认为自己是胜者。作者把全书分成三部分，《红书》中讲述基督教的说法，《绿书》讲述伊斯兰教的说法，《黄书》讲述犹太教说法。哪种说法为真，书中没有明言，留给读者自己去判断。 魔幻线索隐藏在明线之中，需要读者抽丝剥茧。公元9世纪，阿捷赫公主坚守哈扎尔人独有的捕梦者宗教，相信梦中人能在不同人梦里穿越，捕梦者通过采集人的梦，可以整理出关于“第三天神阿丹•鲁阿尼”的知识，从而获得宇宙的秘密，并无限接近上帝。公主和她的爱人各写了一本书，书中讲述捕梦法以及如何获得第三天神神性的方法。这两本书即《哈扎尔辞典》的源头，由两人所写，就有了阴阳本的区别。此书令魔鬼们害怕，他们让公主爱人死去，公主也被剥夺了说话能力，书散失了。那些无意中悟出盗梦真谛的人们曾两次试图将书还原，他们根据梦境和零星线索，分别在1691年和1982年出版了《哈扎尔辞典》，但他们的尝试都被魔鬼阻断了。到1982年，第三天神的神性处于高峰期，三个魔鬼担心三个盗梦人成功收齐辞典，就杀死其中两位，把另一个关进牢房，使这个知识再次成为断片。这些断片汇集成了第二版，也就是如今读者手上的《哈扎尔辞典》。","4","27", "哈扎尔辞典","1")
INSERT INTO `book` (`cat_id`, `book_isbn13`, `book_title`, `book_author`, `book_price`, `book_oprice`, `book_main_image`, `book_grade`, `book_press`, `book_binding`, `book_desc`, `book_degrees`, `book_stock`, `tags`, `book_status`) VALUES( "1","9787500438847","今生今世","胡兰成", "23.80" , "23.80" ," https://img1.doubanio.com/view/subject/m/public/s4368388.jpg", "7.7","中国社会科学出版社","平装","《今生今世》是胡兰成坎坷一生的自传，他到日本后写成，书名为张爱玲所取。书中，他多情地描述了自己的生活和爱情。","5","12", "胡兰成","1")
INSERT INTO `book` (`cat_id`, `book_isbn13`, `book_title`, `book_author`, `book_price`, `book_oprice`, `book_main_image`, `book_grade`, `book_press`, `book_binding`, `book_desc`, `book_degrees`, `book_stock`, `tags`, `book_status`) VALUES( "1","9787563332854","爱与孤独","周国平", "17.80" , "17.80" ," https://img3.doubanio.com/view/subject/m/public/s2166744.jpg", "8.4","广西师范大学出版社","平装","收录散文50余篇，包括《生命本来没有名字》、《女性拯救人类》、《爱情不风流》、《爱与孤独》、《论性爱》等。","3","33", "周国平","1")
INSERT INTO `book` (`cat_id`, `book_isbn13`, `book_title`, `book_author`, `book_price`, `book_oprice`, `book_main_image`, `book_grade`, `book_press`, `book_binding`, `book_desc`, `book_degrees`, `book_stock`, `tags`, `book_status`) VALUES( "1","9787807600558","那件疯狂的小事","庄雅婷", "22.00" , "22.00" ," https://img1.doubanio.com/view/subject/m/public/s2840168.jpg", "7.1","南方出版社","平装","《那件疯狂的小事》是庄雅婷在《MISS格调》开设的情感专栏“庄老师信箱”的结集，专门针对两性情感问题进行答疑解惑。和旧版知心大姐的循循善诱不同，庄老师的文风彪悍凌厉、机锋纵横，大有四两拨千斤之势。无论是面对变态拧巴的爱怨纠缠，还是两性相处中的一地鸡毛，庄老师皆能见招拆招，振聋发聩之余，兼附送额外的幽默与感动。","8","17", "庄雅婷","1")
INSERT INTO `book` (`cat_id`, `book_isbn13`, `book_title`, `book_author`, `book_price`, `book_oprice`, `book_main_image`, `book_grade`, `book_press`, `book_binding`, `book_desc`, `book_degrees`, `book_stock`, `tags`, `book_status`) VALUES( "1","9787530467558","囚徒健身","保罗·威德", "79.00" , "79.00" ," https://img3.doubanio.com/view/subject/m/public/s27248971.jpg", "8.6","北京科学技术出版社","平装","这不是一本教你练出“可爱肌肉”的书，而是一本教你练出能用的力量、极限的力量、生存的力量的书。作者保罗?威德在美国最严酷的监狱中度过了19年，在其中逐渐挖掘出了一套最古老的健身法，在商业社会中早已失传的力量哲学，并凭此成为了地球上最强壮的人之一——这让他得以有尊严地生存下来。出狱之后，他把这套失传的技艺整理并公之于世——这是他带给我们的最珍贵礼物。","2","15", "健身","1")

DROP TABLE IF EXISTS `book_cat`;
SELECT * FROM book_cat

CREATE TABLE `book_cat` (
  `id` INT(11) UNSIGNED NOT NULL AUTO_INCREMENT,
  `book_classify_name` VARCHAR(32) NOT NULL COMMENT '书籍分类名称',
  `weight` TINYINT(4) NOT NULL DEFAULT '1' COMMENT '权重',
  `status` TINYINT(1) NOT NULL DEFAULT '1' COMMENT '状态 1：有效 0：无效',
  `updated_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '最后一次更新时间',
  `created_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '插入时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `idx_classify` (`id`)
) ENGINE=INNODB DEFAULT CHARSET=utf8mb4 COMMENT='图书分类';




DROP TABLE IF EXISTS `book_sale_change_log`;

CREATE TABLE `book_sale_change_log` (
  `id` INT(11) UNSIGNED NOT NULL AUTO_INCREMENT,
  `book_id` INT(11) NOT NULL DEFAULT '0' COMMENT '商品id',
  `quantity` INT(11) NOT NULL DEFAULT '0' COMMENT '售卖数量',
  `price` DECIMAL(10,2) NOT NULL DEFAULT '0.00' COMMENT '售卖金额',
  `member_id` INT(11) NOT NULL DEFAULT '0' COMMENT '会员id',
  `created_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '售卖时间',
  PRIMARY KEY (`id`),
  KEY `idx_bood_sale` (`book_id`)
) ENGINE=INNODB DEFAULT CHARSET=utf8mb4 COMMENT='商品销售情况';




DROP TABLE IF EXISTS `book_stock_change_log`;

CREATE TABLE `book_stock_change_log` (
  `id` INT(11) UNSIGNED NOT NULL AUTO_INCREMENT,
  `book_id` INT(11) NOT NULL COMMENT '商品id',
  `unit` INT(11) NOT NULL DEFAULT '0' COMMENT '变更多少',
  `residue` INT(11) NOT NULL DEFAULT '0' COMMENT '变更之后总量',
  `note` VARCHAR(100) NOT NULL DEFAULT '' COMMENT '备注字段',
  `created_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '插入时间',
  PRIMARY KEY (`id`),
  KEY `idx_book_stock` (`book_id`)
) ENGINE=INNODB DEFAULT CHARSET=utf8mb4 COMMENT='数据库存变更表';



DROP TABLE IF EXISTS `images`;

CREATE TABLE `images` (
  `id` INT(11) UNSIGNED NOT NULL AUTO_INCREMENT,
  `file_key` VARCHAR(60) NOT NULL DEFAULT '' COMMENT '文件名',
  `created_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '插入时间',
  PRIMARY KEY (`id`)
) ENGINE=INNODB DEFAULT CHARSET=utf8mb4;

SELECT * FROM app_access_log
DROP TABLE IF EXISTS `member_address`;
SELECT * FROM member_address

CREATE TABLE `member_address` (
  `id` INT(11) UNSIGNED NOT NULL AUTO_INCREMENT,
  `member_id` INT(11) NOT NULL DEFAULT '0' COMMENT '会员id',
  `nickname` VARCHAR(20) NOT NULL DEFAULT '' COMMENT '收货人姓名',
  `mobile` VARCHAR(11) NOT NULL DEFAULT '' COMMENT '收货人手机号码',
  `province_id` INT(6) NOT NULL DEFAULT '0' COMMENT '省id',
  `province_str` VARCHAR(10) NOT NULL DEFAULT '' COMMENT '省名称',
  `city_id` INT(6) NOT NULL DEFAULT '0' COMMENT '城市id',
  `city_str` VARCHAR(10) NOT NULL DEFAULT '' COMMENT '市名称',
  `dist_id` INT(6) NOT NULL DEFAULT '0' COMMENT '区域id',
  `dist_str` VARCHAR(10) NOT NULL DEFAULT '' COMMENT '区域名称',
  `address` VARCHAR(50) NOT NULL DEFAULT '' COMMENT '详细地址',
  `status` TINYINT(1) NOT NULL DEFAULT '1' COMMENT '是否有效 1：有效 0：无效',
  `is_default` TINYINT(1)  NOT NULL  DEFAULT '0'  COMMENT '默认地址',
  `updated_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '最后一次更新时间',
  `created_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '插入时间',
  PRIMARY KEY (`id`),
  KEY `idx_member_id_status` (`member_id`,`status`)
) ENGINE=INNODB DEFAULT CHARSET=utf8mb4 COMMENT='会员收货地址';


SELECT*FROM book

DROP TABLE IF EXISTS `member_cart`;
SELECT * FROM member_cart
CREATE TABLE `member_cart` (
  `id` INT(11) UNSIGNED NOT NULL AUTO_INCREMENT,
  `member_id` BIGINT(20) NOT NULL DEFAULT '0' COMMENT '会员id',
  `book_id` INT(11) NOT NULL DEFAULT '0' COMMENT '商品id',
  `quantity` INT(11) NOT NULL DEFAULT '0' COMMENT '数量',
  `updated_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '最后一次更新时间',
  `created_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '插入时间',
  PRIMARY KEY (`id`),
  KEY `idx_member_cart` (`member_id`)
) ENGINE=INNODB DEFAULT CHARSET=utf8mb4 COMMENT='购物车';



DROP TABLE IF EXISTS `wx_share_history`;

SELECT * FROM wx_share_history
CREATE TABLE `wx_share_history` (
  `id` INT(11) UNSIGNED NOT NULL AUTO_INCREMENT,
  `member_id` INT(11) NOT NULL DEFAULT '0' COMMENT '会员id',
  `share_url` VARCHAR(200) NOT NULL DEFAULT '' COMMENT '分享的页面url',
  `created_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  PRIMARY KEY (`id`)
) ENGINE=INNODB DEFAULT CHARSET=utf8mb4 COMMENT='微信分享记录';



DROP TABLE IF EXISTS `member_comments`;

CREATE TABLE `member_comments` (
  `id` INT(11) UNSIGNED NOT NULL AUTO_INCREMENT,
  `member_id` INT(11) NOT NULL DEFAULT '0' COMMENT '会员id',
  `book_ids` VARCHAR(200) NOT NULL DEFAULT '' COMMENT '商品ids',
  `pay_order_id` INT(11) NOT NULL DEFAULT '0' COMMENT '订单id',
  `score` TINYINT(4) NOT NULL DEFAULT '0' COMMENT '评分',
  `content` VARCHAR(200) NOT NULL DEFAULT '' COMMENT '评论内容',
  `created_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '插入时间',
  PRIMARY KEY (`id`),
  KEY `idx_member_id` (`member_id`)
) ENGINE=INNODB DEFAULT CHARSET=utf8mb4 COMMENT='会员评论表';


DROP TABLE IF EXISTS `pay_order`;

CREATE TABLE `pay_order` (
  `id` INT(11) UNSIGNED NOT NULL AUTO_INCREMENT,
  `order_sn` VARCHAR(40) NOT NULL DEFAULT '' COMMENT '随机订单号',
  `member_id` BIGINT(11) NOT NULL DEFAULT '0' COMMENT '会员id',
  `total_price` DECIMAL(10,2) NOT NULL DEFAULT '0.00' COMMENT '订单应付金额',
  `yun_price` DECIMAL(10,2) NOT NULL DEFAULT '0.00' COMMENT '运费金额',
  `pay_price` DECIMAL(10,2) NOT NULL DEFAULT '0.00' COMMENT '订单实付金额',
  `pay_sn` VARCHAR(128) NOT NULL DEFAULT '' COMMENT '第三方流水号',
  `prepay_id` VARCHAR(128) NOT NULL DEFAULT '' COMMENT '第三方预付id',
  `note` TEXT NOT NULL COMMENT '备注信息',
  `status` TINYINT(4) NOT NULL DEFAULT '0' COMMENT '1：支付完成 0 无效 -1 申请退款 -2 退款中 -9 退款成功  -8 待支付  -7 完成支付待确认',
  `express_status` TINYINT(4) NOT NULL DEFAULT '0' COMMENT '快递状态，-8 待支付 -7 已付款待发货 1：确认收货 0：失败',
  `express_address_id` INT(11) NOT NULL DEFAULT '0' COMMENT '快递地址id',
  `express_info` VARCHAR(1000) NOT NULL DEFAULT '' COMMENT '快递信息',
  `comment_status` TINYINT(1) NOT NULL DEFAULT '0' COMMENT '评论状态',
  `pay_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '付款到账时间',
  `updated_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '最近一次更新时间',
  `created_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '插入时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `idx_order_sn` (`order_sn`),
  KEY `idx_member_id_status` (`member_id`,`status`)
) ENGINE=INNODB DEFAULT CHARSET=utf8mb4 COMMENT='购买订单表';


DROP TABLE IF EXISTS `pay_order_item`;

CREATE TABLE `pay_order_item` (
  `id` INT(11) UNSIGNED NOT NULL AUTO_INCREMENT,
  `pay_order_id` INT(11) NOT NULL DEFAULT '0' COMMENT '订单id',
  `member_id` BIGINT(11) NOT NULL DEFAULT '0' COMMENT '会员id',
  `quantity` INT(11) NOT NULL DEFAULT '1' COMMENT '购买数量 默认1份',
  `price` DECIMAL(10,2) NOT NULL DEFAULT '0.00' COMMENT '商品总价格，售价 * 数量',
  `book_id` INT(11) NOT NULL DEFAULT '0' COMMENT '商品id',
  `note` TEXT NOT NULL COMMENT '备注信息',
  `status` TINYINT(1) NOT NULL DEFAULT '1' COMMENT '状态：1：成功 0 失败',
  `updated_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '最近一次更新时间',
  `created_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '插入时间',
  PRIMARY KEY (`id`),
  KEY `id_order_id` (`pay_order_id`),
  KEY `idx_book_id` (`book_id`)
) ENGINE=INNODB DEFAULT CHARSET=utf8mb4 COMMENT='订单详情表';



DROP TABLE IF EXISTS `pay_order_callback_data`;

CREATE TABLE `pay_order_callback_data` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `pay_order_id` INT(11) NOT NULL DEFAULT '0' COMMENT '支付订单id',
  `pay_data` TEXT NOT NULL COMMENT '支付回调信息',
  `refund_data` TEXT NOT NULL COMMENT '退款回调信息',
  `updated_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '最后一次更新时间',
  `created_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `pay_order_id` (`pay_order_id`)
) ENGINE=INNODB DEFAULT CHARSET=utf8mb4;




DROP TABLE IF EXISTS `queue_list`;

CREATE TABLE `queue_list` (
  `id` INT(11) UNSIGNED NOT NULL AUTO_INCREMENT,
  `queue_name` VARCHAR(30) NOT NULL DEFAULT '' COMMENT '队列名字',
  `data` VARCHAR(500) NOT NULL DEFAULT '' COMMENT '队列数据',
  `status` TINYINT(1) NOT NULL DEFAULT '-1' COMMENT '状态 -1 待处理 1 已处理',
  `updated_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '最后一次更新时间',
  `created_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '插入时间',
  PRIMARY KEY (`id`)
) ENGINE=INNODB DEFAULT CHARSET=utf8mb4 COMMENT='事件队列表';


DROP TABLE IF EXISTS `oauth_access_token`;

CREATE TABLE `oauth_access_token` (
  `id` INT(11) UNSIGNED NOT NULL AUTO_INCREMENT,
  `access_token` VARCHAR(600) NOT NULL DEFAULT '',
  `expired_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '过期时间',
  `created_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '插入时间',
  PRIMARY KEY (`id`),
  KEY `idx_expired_time` (`expired_time`)
) ENGINE=INNODB DEFAULT CHARSET=utf8mb4 COMMENT='微信的access_token 用户调用其他接口的';



DROP TABLE IF EXISTS `stat_daily_food`;
SELECT * FROM stat_daily_food
CREATE TABLE `stat_daily_book` (
  `id` INT(11) UNSIGNED NOT NULL AUTO_INCREMENT,
  `date` DATE NOT NULL,
  `book_id` INT(11) NOT NULL DEFAULT '0' COMMENT '商品id',
  `total_count` INT(11) NOT NULL DEFAULT '0' COMMENT '售卖总数量',
  `total_pay_money` DECIMAL(10,2) NOT NULL DEFAULT '0.00' COMMENT '总售卖金额',
  `updated_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '最后一次更新时间',
  `created_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '插入时间',
  PRIMARY KEY (`id`),
  KEY `date_book_id` (`date`,`book_id`)
) ENGINE=INNODB DEFAULT CHARSET=utf8mb4 COMMENT='书籍售卖日统计';


DROP TABLE IF EXISTS `stat_daily_member`;

SELECT * FROM stat_daily_member
CREATE TABLE `stat_daily_member` (
  `id` INT(11) UNSIGNED NOT NULL AUTO_INCREMENT,
  `date` DATE NOT NULL COMMENT '日期',
  `member_id` INT(11) NOT NULL DEFAULT '0' COMMENT '会员id',
  `total_shared_count` INT(11) NOT NULL DEFAULT '0' COMMENT '当日分享总次数',
  `total_pay_money` DECIMAL(10,2) NOT NULL DEFAULT '0.00' COMMENT '当日付款总金额',
  `updated_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '最后一次更新时间',
  `created_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '插入时间',
  PRIMARY KEY (`id`),
  KEY `idx_date_member_id` (`date`,`member_id`)
) ENGINE=INNODB DEFAULT CHARSET=utf8mb4 COMMENT='会员日统计';


DROP TABLE IF EXISTS `stat_daily_site`;

SELECT * FROM stat_daily_site
CREATE TABLE `stat_daily_site` (
  `id` INT(11) UNSIGNED NOT NULL AUTO_INCREMENT,
  `date` DATE NOT NULL COMMENT '日期',
  `total_pay_money` DECIMAL(10,2) NOT NULL DEFAULT '0.00' COMMENT '当日应收总金额',
  `total_member_count` INT(11) NOT NULL COMMENT '会员总数',
  `total_new_member_count` INT(11) NOT NULL COMMENT '当日新增会员数',
  `total_order_count` INT(11) NOT NULL COMMENT '当日订单数',
  `total_shared_count` INT(11) NOT NULL,
  `updated_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '最后一次更新时间',
  `created_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '插入时间',
  PRIMARY KEY (`id`),
  KEY `idx_date` (`date`)
) ENGINE=INNODB DEFAULT CHARSET=utf8mb4 COMMENT='全站日统计';











