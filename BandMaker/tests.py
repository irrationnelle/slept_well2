from django.test import TestCase
from Session.models import Instrument
from Applicants.models import MyUser
from Session.models import Session

class InstTest(TestCase):
    def setUp(self):
        i1 = Instrument.objects.create(name='bass')
        i1.save()
        i2 = Instrument.objects.create(name='guitar')
        i2.save()

        u1 = MyUser.objects.create(email='isenfenriz@naver.com', nickname='rase')
        u1.save()
        u2 = MyUser.objects.create(email='drakkarverenis@gmail.com', nickname='verenis')
        u2.save()

        s1 = Session.objects.create(players=u1)
        s1.save()
        s1.instruments.add(i1)
        s1.save()

        s2 = Session.objects.create(players=u2)
        s2.save()
        s2.instruments.create(name='drum')
        s2.save()

    def test_example(self):
        bass = Instrument.objects.get(name='bass')
        guitar = Instrument.objects.get(name='guitar')
        user = MyUser.objects.get(nickname='rase')
        player = Session.objects.get(players=user)
        self.assertEqual('bass', bass.name)
        self.assertEqual('rase', player.players.nickname)
        self.assertEqual('bass', player.instruments.all()[0].name)

        # session = Session.objects.all()
        # print(session[0].players.nickname)
        # print(session[1].players)
        #
        # print(session[1].instruments.name)

        # sessionInst = Session.instruments.all()
        # for s in sessionInst:
        #     print(s.groups.all())