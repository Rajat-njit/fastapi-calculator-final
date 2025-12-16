"""
Calculation Models Module

This module defines the database models and business logic for user calculations.
It uses SQLAlchemy polymorphic inheritance to support multiple calculation types
(addition, subtraction, multiplication, etc.) under a single table.

Key design patterns used:
- Polymorphic ORM inheritance
- Factory pattern for calculation creation
- Strong input validation inside operation logic
"""

from datetime import datetime
import uuid
from sqlalchemy import Column, String, DateTime, ForeignKey, JSON, Float
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship, declared_attr

from app.database import Base


# ------------------------------------------------------------------------------
# Abstract Base Calculation
# ------------------------------------------------------------------------------

class AbstractCalculation:
    """
    Abstract base class defining shared columns for all calculations.

    This class is NOT mapped directly to a table. Instead, it provides
    common columns that are inherited by the Calculation model.
    """

    @declared_attr
    def __tablename__(cls):
        return "calculations"

    @declared_attr
    def id(cls):
        return Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    @declared_attr
    def user_id(cls):
        return Column(
            UUID(as_uuid=True),
            ForeignKey("users.id", ondelete="CASCADE"),
            nullable=False,
            index=True
        )

    @declared_attr
    def type(cls):
        """
        Polymorphic discriminator column.
        Determines which calculation subclass is used.
        """
        return Column(String(50), nullable=False, index=True)

    @declared_attr
    def inputs(cls):
        """
        Stores calculation inputs as JSON (list of numbers).
        """
        return Column(JSON, nullable=False)

    @declared_attr
    def result(cls):
        """
        Stores the computed result of the calculation.
        """
        return Column(Float, nullable=True)

    @declared_attr
    def created_at(cls):
        return Column(DateTime, default=datetime.utcnow, nullable=False)

    @declared_attr
    def updated_at(cls):
        return Column(
            DateTime,
            default=datetime.utcnow,
            onupdate=datetime.utcnow,
            nullable=False
        )


# ------------------------------------------------------------------------------
# Base Calculation Model
# ------------------------------------------------------------------------------

class Calculation(Base, AbstractCalculation):
    """
    Base Calculation ORM model.

    This class acts as the parent for all calculation types
    and enables SQLAlchemy polymorphic behavior.
    """

    __mapper_args__ = {
        "polymorphic_on": "type",
        "polymorphic_identity": "calculation",
    }

    # Relationship back to the owning user
    user = relationship("User", back_populates="calculations")

    def __repr__(self):
        return f"<Calculation(type={self.type}, inputs={self.inputs})>"

    # --------------------------------------------------------------------------
    # Factory Method
    # --------------------------------------------------------------------------

    @staticmethod
    def create(calculation_type: str, user_id, inputs):
        """
        Factory method to create a calculation instance based on type.

        This method centralizes calculation creation logic and ensures
        only supported calculation types are instantiated.

        Args:
            calculation_type (str): Name of the calculation type
            user_id (UUID): ID of the owning user
            inputs (list): List of numeric inputs

        Returns:
            Calculation: Instance of a specific calculation subclass

        Raises:
            ValueError: If calculation type is invalid or unsupported
        """

        if not isinstance(calculation_type, str):
            raise ValueError("Unsupported calculation type")

        calc_key = calculation_type.strip().lower()

        mapping = {
            "addition": Addition,
            "subtraction": Subtraction,
            "multiplication": Multiplication,
            "division": Division,
            "exponentiation": Exponentiation,
            "power": Power,
            "modulus": Modulus,
        }

        cls = mapping.get(calc_key)
        if cls is None:
            raise ValueError("Unsupported calculation type")

        return cls(user_id=user_id, inputs=inputs)


# ------------------------------------------------------------------------------
# Calculation Subclasses (Polymorphic Operations)
# ------------------------------------------------------------------------------

class Addition(Calculation):
    __mapper_args__ = {"polymorphic_identity": "addition"}

    def get_result(self):
        if not isinstance(self.inputs, list):
            raise ValueError("Inputs must be a list of numbers.")
        if len(self.inputs) < 2:
            raise ValueError("Inputs must contain at least two numbers.")
        return sum(self.inputs)


class Subtraction(Calculation):
    __mapper_args__ = {"polymorphic_identity": "subtraction"}

    def get_result(self):
        if not isinstance(self.inputs, list):
            raise ValueError("Inputs must be a list of numbers.")
        if len(self.inputs) < 2:
            raise ValueError("Inputs must contain at least two numbers.")

        result = self.inputs[0]
        for value in self.inputs[1:]:
            result -= value
        return result


class Multiplication(Calculation):
    __mapper_args__ = {"polymorphic_identity": "multiplication"}

    def get_result(self):
        if not isinstance(self.inputs, list):
            raise ValueError("Inputs must be a list of numbers.")
        if len(self.inputs) < 2:
            raise ValueError("Inputs must contain at least two numbers.")

        result = 1
        for value in self.inputs:
            result *= value
        return result


class Division(Calculation):
    __mapper_args__ = {"polymorphic_identity": "division"}

    def get_result(self):
        if not isinstance(self.inputs, list):
            raise ValueError("Inputs must be a list of numbers.")
        if len(self.inputs) < 2:
            raise ValueError("Inputs must contain at least two numbers.")

        result = self.inputs[0]
        for value in self.inputs[1:]:
            if value == 0:
                raise ValueError("Cannot divide by zero.")
            result /= value
        return result


class Exponentiation(Calculation):
    __mapper_args__ = {"polymorphic_identity": "exponentiation"}

    def get_result(self):
        if not isinstance(self.inputs, list):
            raise ValueError("Inputs must be a list with at least two numbers.")

        result = self.inputs[0]
        for value in self.inputs[1:]:
            result **= value
        return float(result)


class Power(Calculation):
    __mapper_args__ = {"polymorphic_identity": "power"}

    def get_result(self):
        if not isinstance(self.inputs, list):
            raise ValueError("Inputs must be a list of numbers.")
        if len(self.inputs) != 2:
            raise ValueError("Power requires exactly two values.")

        return float(self.inputs[0] ** self.inputs[1])


class Modulus(Calculation):
    __mapper_args__ = {"polymorphic_identity": "modulus"}

    def get_result(self):
        if not isinstance(self.inputs, list):
            raise ValueError("Inputs must be a list of numbers.")
        if len(self.inputs) != 2:
            raise ValueError("Modulus requires exactly two values.")
        if self.inputs[1] == 0:
            raise ValueError("Modulus by zero is undefined.")

        return float(self.inputs[0] % self.inputs[1])
