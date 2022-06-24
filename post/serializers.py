from rest_framework import serializers
from post.models import Company as CompanyModel
from post.models import JobPost as JobPostModel
from post.models import JobPostSkillSet as JobPostSkillSetModel


class CompanySerializers(serializers.ModelSerializer):
    class Meta:
        model = CompanyModel
        fields = ["company_name"]


class JobPostSerializers(serializers.ModelSerializer):
    class Meta:
        model = JobPostModel
        fields = ["job_description", "created_at", "job_type", "company", "salary"]        


class JobPostSkillSetSerializers(serializers.ModelSerializer):
    class Meta:
        model = JobPostSkillSetModel
        fields = ["job_post", "skill_set"]