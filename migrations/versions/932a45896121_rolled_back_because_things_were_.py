"""rolled back because things were suddenly acting funny

Revision ID: 932a45896121
Revises: b91419ccca4e
Create Date: 2022-05-10 17:55:37.308543

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '932a45896121'
down_revision = 'b91419ccca4e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('task_goal_id_fkey', 'task', type_='foreignkey')
    op.drop_column('task', 'goal_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('task', sa.Column('goal_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('task_goal_id_fkey', 'task', 'goal', ['goal_id'], ['goal_id'])
    # ### end Alembic commands ###
