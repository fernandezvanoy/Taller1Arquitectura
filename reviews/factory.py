from .models import PositiveReview, NegativeReview, NeutralReview 

class ReviewFactory:
    @staticmethod
    def create_review(user, product, rating, comment):
        if rating >= 4:
            return PositiveReview.objects.create(user=user, product=product, rating=rating, comment=comment)
        elif rating == 3:
            return NeutralReview.objects.create(user=user, product=product, rating=rating, comment=comment)
        else:
            return NegativeReview.objects.create(user=user, product=product, rating=rating, comment=comment)
