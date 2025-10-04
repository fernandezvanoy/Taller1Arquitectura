from .models import PositiveReview, NegativeReview, NeutralReview 

class ReviewProxy:
    @classmethod
    def create_review(cls, user, product, rating, comment):
        if rating >= 4:
            review = PositiveReview(user=user, product=product, rating=rating, comment=comment)
        elif rating == 3:
            review = NeutralReview(user=user, product=product, rating=rating, comment=comment)
        else:
            review = NegativeReview(user=user, product=product, rating=rating, comment=comment)
        review.save()
        return review
