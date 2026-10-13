from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Category, Course


class CourseFlowTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.owner = User.objects.create_user(username="teacher", password="test-only-password")
        cls.other = User.objects.create_user(username="other", password="test-only-password")
        cls.backend = Category.objects.create(name="Backend", slug="backend")
        cls.frontend = Category.objects.create(name="Frontend", slug="frontend")
        cls.course = Course.objects.create(teacher=cls.owner, category=cls.backend,
                                          name="Django temelleri", slug="django-temelleri")
        Course.objects.create(teacher=cls.owner, category=cls.frontend,
                              name="Arayüz tasarımı", slug="arayuz-tasarimi")

    def test_course_list_filters_by_category(self):
        response = self.client.get(reverse("courses_by_category", args=["backend"]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual([course.pk for course in response.context["courses"]], [self.course.pk])

    def test_course_detail_and_missing_course(self):
        response = self.client.get(reverse("course_detail", args=["backend", self.course.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["course"], self.course)
        self.assertEqual(self.client.get(reverse("course_detail", args=["backend", "missing"])).status_code, 404)

    def test_anonymous_cannot_create_course(self):
        response = self.client.post(reverse("create_course"), {"name": "Unauthorized"})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Course.objects.count(), 2)

    def test_other_teacher_cannot_update_course(self):
        self.client.force_login(self.other)
        response = self.client.post(reverse("update_course", args=[self.course.slug]),
                                    {"name": "Changed", "category": self.backend.pk})
        self.assertEqual(response.status_code, 404)
        self.course.refresh_from_db()
        self.assertEqual(self.course.name, "Django temelleri")

    def test_other_teacher_cannot_delete_course(self):
        self.client.force_login(self.other)
        response = self.client.post(reverse("delete_course", args=[self.course.slug]))
        self.assertEqual(response.status_code, 404)
        self.assertTrue(Course.objects.filter(pk=self.course.pk).exists())

    def test_owner_can_delete_own_course(self):
        self.client.force_login(self.owner)
        response = self.client.post(reverse("delete_course", args=[self.course.slug]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Course.objects.filter(pk=self.course.pk).exists())
