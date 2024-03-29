# В большой текстовой строке подсчитать количество встречаемых слов и
# вернуть 10 самых частых. Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.

import re
from collections import Counter


def word_frequency(input_text: str) -> list:
    """подсчитывает количество встречаемости слов в тексте без учета регистра"""
    input_text = re.sub(r'[^\w\s]', '', input_text)
    input_text = input_text.replace("\n", "").lower().split(" ")
    count_list = Counter(input_text)
    return sorted(count_list.items(), key=lambda x: x[1])


text = '''
В 2010 году Патрик Маккензи написал знаменитую статью «Заблуждения программистов об именах», перечислив 40 фактоидов, которые не всегда верны в отношении человеческих имён.

Думаете, программисты сели, подумали и изменили обработку имён в компьютерных системах? К сожалению, не совсем. Нас по-прежнему повсеместно просят заполнить онлайн-формы, которые предполагают обязательное наличие имени и фамилии (причём именно в таком порядке). Эти системы по-прежнему предполагают, что наши имена всегда можно записать символами алфавита, зачастую только ASCII.

Подозреваю, что статья Патрика оказала недостаточное влияние на индустрию в том числе потому, что в ней отсутствовали примеры каждого заблуждения. Но как бывший сотрудник проекта IBM Global Name Management могу вас заверить, что всё всё сказанное в ней — правда.

Не верите? В этой статье я перечислю все 40 заблуждений, приведя пример (или два) из моего опыта работы в этой области. Готовы? Поехали!

1. У каждого человека есть одно каноническое полное имя.
Кажется, некоторые люди считают, что вы получаете имя, и оно никогда не меняется. Но даже в западных странах человек может изменить свою фамилию при вступлении в брак. В католической традиции человек может получить второе имя при конфирмации.

2. У каждого человека есть одно полное имя, которое он использует.
Хорошо известный писатель-фантаст Джон Уиндем (автор «Дня Триффидов») рождён с именем Джон Уиндем Паркс Лукас Бейнон Харрис, а публиковал книги под именами Джон Бейнон и Лукас Паркс, а также Джон Уиндем.

3. В данный момент времени у каждого человека есть одно каноническое полное имя.
У актёра может быть сценический псевдоним, полностью отличающийся от имени в свидетельстве о рождении, у него может быть даже паспорт на сценический псевдоним.

4. В данный момент времени у каждого человека одно полное имя, которое он использует.
Это не так, даже в западных странах женщина может сохранить девичью фамилию на работе (где она уже известна под этим именем) и использовать фамилию мужа в общении или в юридических документах, таких как ипотека и кредиты.
5. У каждого человека есть в точности N имён, независимо от значения N.
Английское имя традиционно содержит два имени (их часто называют именем и вторым именем) и фамилию, но не обязательно всё именно так. У человека может не быть второго имени или их может быть несколько. Например, у португальцев одно или два имени и до четырёх фамилий (до шести в случае замужней женщины), и эти фамилии могут быть фразами, такими как да Силва или дос Сантуш, или даже Коста-и-Силва.

6. Имена вмещаются в определённое количество символов.
У известного художника, которого обычно зовут просто Пикассо, полное имя было Пабло Диего Хосе Франсиско де Паула Хуан Непомусено Мария де лос Ремедиос Сиприано де ла Сантисима Тринидад Мартир Патрисио Руис и Пикассо. Попробуйте вместить это в форму на 30 символов…

7. Имена не меняются.
Мы уже упоминали о девушках, которые меняют имя при вступлении в брак, так что это явно неверно. Кроме того, католики могут принять второе имя в момент конфирмации. Также человек часто добавляет имя или полностью меняет его при переходе в другую религию — вспомните, как после обращения в ислам Кэт Стивенс стал Юсуфом Исламом, а Кассиус Клей превратился в Мохаммеда Али.

8. Имена меняются, но только в определённых ограниченных случаях.
Для некоторых тайцев обычное дело сменить имя, чтобы отогнать неудачу. Это может произойти без особого повода. Иногда человек меняет имя, когда кто-то другой с таким же именем стал известным или печально известным: примечательный пример, когда множество людей отказалось от фамилии Гитлер.

9. Имена записаны в ASCII.
Явное заблуждение хотя бы потому, что ASCII не содержит акцентированные символы из французских, португальских имён. Этот набор символов не включает греческий алфавит, используемый в греческих именах, кириллические символы для русских имен. Есть письменности вроде деванагари для индийских имен, китайские иероглифы (ханзи), японские иероглифы (кандзи), и многое другое.

10. Имена записаны в какой-нибудь одной кодировке.
В некоторых именах смешаны кодировки. Например, кандзи с латинскими символами или ханзи с латинскими символами, или корейский хангыль с латинскими символами. Во многих случаях это происходит потому что у человека есть «западное имя» в угоду тем, кто не может произнести его имя на его родном языке.'''

print(word_frequency(text)[-1:-11:-1])
