"""Add nullable false for all field except pet photo

Revision ID: 97816a1398d1
Revises: ff36453c4c77
Create Date: 2021-08-05 20:47:56.740643

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '97816a1398d1'
down_revision = 'ff36453c4c77'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('pets', 'name_pet',
               existing_type=sa.VARCHAR(length=250),
               nullable=False)
    op.alter_column('pets', 'pet_owner_name',
               existing_type=sa.VARCHAR(length=250),
               nullable=False)
    op.alter_column('pets', 'breed',
               existing_type=sa.VARCHAR(length=250),
               nullable=False)
    op.alter_column('pets', 'birth_date',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('pets', 'birth_date',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('pets', 'breed',
               existing_type=sa.VARCHAR(length=250),
               nullable=True)
    op.alter_column('pets', 'pet_owner_name',
               existing_type=sa.VARCHAR(length=250),
               nullable=True)
    op.alter_column('pets', 'name_pet',
               existing_type=sa.VARCHAR(length=250),
               nullable=True)
    # ### end Alembic commands ###