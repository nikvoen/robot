from django.core.exceptions import ValidationError
from django.test import TestCase
from events.models import ClassicEvent, Questionnaire


class ModelTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.classic_event = ClassicEvent.objects.create(
            link_to_the_registr='https://test-classic-event-link',
            name='test',
            description='test description',
            link_to_photo_album='https://test-link',
            link_to_the_docs='https://test-link',
            venue='place',
        )

    def tearDown(self):
        Questionnaire.objects.all().delete()
        super().tearDown()

    def test_wrong_group(self):
        questionnaire_count = Questionnaire.objects.count()
        group_endpoints = [
            'ИУ9- 12Б',
            'ИУ9 - 12Б',
            'ИУ 9-12Б',
            'ИУ-12Б',
            'ИУ-122Б',
        ]
        for group in group_endpoints:
            Questionnaire.objects.all().delete()
            with self.subTest(
                 f'This group must fail validation'
                 f' - "{group}"',
                 ):
                with self.assertRaises(ValidationError):
                    self.questionnaire = Questionnaire(
                        full_name='Иванов Иван Иванович',
                        group=group,
                        number_of_people=5,
                        required_competencies='test',
                        link_to_vk='https://vk.com',
                        additional_information='test',
                        classic_event=self.classic_event,
                    )
                    self.questionnaire.full_clean()
                    self.questionnaire.save()

                self.assertEqual(Questionnaire.objects.count(),
                                 questionnaire_count)

    def test_right_group(self):
        questionnaire_count = Questionnaire.objects.count()
        group_endpoints = [
            'ИУ9-12Б',
            'ФН12-12БВ',
            'ИСОТ2-11М',
            'Э8-31',
            'СГН2-51Б',
        ]
        for group in group_endpoints:
            Questionnaire.objects.all().delete()
            with self.subTest(
                 f'The model with such group must be created'
                 f' - "{group}"',
                 ):

                self.questionnaire = Questionnaire(
                    full_name='Иванов Иван Иванович',
                    group=group,
                    number_of_people=5,
                    required_competencies='test',
                    link_to_vk='https://vk.com',
                    additional_information='test',
                    classic_event=self.classic_event,
                )
                self.questionnaire.full_clean()
                self.questionnaire.save()

                self.assertEqual(Questionnaire.objects.count(),
                                 questionnaire_count + 1)

    def test_right_full_name(self):
        questionnaire_count = Questionnaire.objects.count()
        full_name_endpoints = [
            'Иванов Иван Иванович',
            'Аля-Вавилова Антонина Сергеевна',
            'Буб Лев Антонович',
            'Джо Блэк',
        ]
        for full_name in full_name_endpoints:
            Questionnaire.objects.all().delete()
            with self.subTest(
                 f'The model with such full name must be created'
                 f' - "{full_name}"',
                 ):

                self.questionnaire = Questionnaire(
                    full_name=full_name,
                    group='ИУ9-12Б',
                    number_of_people=5,
                    required_competencies='test',
                    link_to_vk='https://vk.com',
                    additional_information='test',
                    classic_event=self.classic_event,
                )
                self.questionnaire.full_clean()
                self.questionnaire.save()

                self.assertEqual(Questionnaire.objects.count(),
                                 questionnaire_count + 1)

    def test_wrong_full_name(self):
        questionnaire_count = Questionnaire.objects.count()
        full_name_endpoints = [
            'Иванов',
            'Буб-Лев-Антонович',
            'БубЛевАнтонович',
        ]
        for full_name in full_name_endpoints:
            Questionnaire.objects.all().delete()
            with self.subTest(
                 f'This full name must fail validation'
                 f' - "{full_name}"',
                 ):
                with self.assertRaises(ValidationError):
                    self.questionnaire = Questionnaire(
                        full_name=full_name,
                        group='ИУ9-12Б',
                        number_of_people=5,
                        required_competencies='test',
                        link_to_vk='https://vk.com',
                        additional_information='test',
                        classic_event=self.classic_event,
                    )
                    self.questionnaire.full_clean()
                    self.questionnaire.save()

                self.assertEqual(Questionnaire.objects.count(),
                                 questionnaire_count)
