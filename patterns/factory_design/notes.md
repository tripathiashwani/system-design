# Abstract Factory Design Pattern

## Definition

Abstract Factory Pattern is a **creational design pattern** used to create **families of related objects** without specifying their concrete classes.

It provides an interface for creating multiple related objects together.

---

## Simple Idea

Think of it like:

> One factory creates multiple related products.

Example:

### Product Types

* Burger
* Garlic Bread
* Drink

### Product Families

* Singh Burger Family
* King Burger Family

So:

* **Singh Factory** creates:

  * Singh Burger
  * Singh Garlic Bread
  * Singh Drink

* **King Factory** creates:

  * King Burger
  * King Garlic Bread
  * King Drink

---

# When to Use Abstract Factory

---

## 1. When objects belong to a family and should be used together

Use it when products are related and must remain compatible.

### Example:

In burger system:

* Singh burgers use normal bread
* King burgers use wheat bread

Bad combination:

```python
burger = PremiumBurger()
garlic = BasicWheatGarlicBread()
```

This mixes two different families.

Using Abstract Factory ensures consistency.

Example:

```python
factory = SinghFactory()
burger = factory.create_burger()
garlic = factory.create_garlic_bread()
```

### Use when:

* Products are related
* Products should be used together

---

## 2. When application supports multiple themes/configurations

Very common in UI systems.

### Example:

Themes:

* Light Theme
* Dark Theme

Products:

* Button
* Checkbox
* Menu

Factories:

* LightThemeFactory
* DarkThemeFactory

Light Factory creates:

* LightButton
* LightCheckbox
* LightMenu

Dark Factory creates:

* DarkButton
* DarkCheckbox
* DarkMenu

Example:

```python
factory = DarkThemeFactory()
button = factory.create_button()
menu = factory.create_menu()
```

### Use when:

* Same system supports multiple themes/configurations

---

## 3. When you want loose coupling

Without Abstract Factory:

```python
button = WindowsButton()
menu = WindowsMenu()
```

Client depends directly on concrete classes.

With Abstract Factory:

```python
factory = WindowsFactory()
button = factory.create_button()
menu = factory.create_menu()
```

Benefits:

* Less dependency
* Better maintainability
* Easier testing

### Use when:

* You want to hide object creation details

---

## 4. When new product families are added frequently

Example:

Current families:

* Windows
* Mac

Future family:

* Linux

Without Abstract Factory:
You modify many parts of code.

With Abstract Factory:
Just add:

```python
class LinuxFactory:
    pass
```

Existing code remains unchanged.

### Use when:

* New product families are frequently added

---

## 5. When object creation depends on environment/configuration

Example: Database systems

Factories:

* MySQLFactory
* PostgreSQLFactory
* MongoFactory

Products:

* Connection
* QueryExecutor
* TransactionManager

Example:

```python
factory = PostgreSQLFactory()
conn = factory.create_connection()
query = factory.create_query_executor()
```

### Use when:

* Product family depends on environment/configuration

---

# Real World Examples

---

## GUI Frameworks

Factories:

* WindowsFactory
* MacFactory

Products:

* Button
* Menu
* Scrollbar

---

## Database Drivers

Factories:

* MySQLFactory
* PostgreSQLFactory

Products:

* Connection
* QueryExecutor

---

## Cloud Providers

Factories:

* AWSFactory
* AzureFactory
* GCPFactory

Products:

* Storage
* Compute
* Monitoring

Example:

* AWS → S3, EC2, CloudWatch
* Azure → Blob, VM, Monitor

---

## Notification Systems

Factories:

* EmailFactory
* SMSFactory
* PushFactory

Products:

* Sender
* Formatter
* Validator

---

# When NOT to Use Abstract Factory

Do NOT use Abstract Factory when:

* You only create one type of object
* Products are not related
* Simple Factory is enough

Example:

```python
vehicle = VehicleFactory.create("car")
```

This is Factory Method, not Abstract Factory.

---

# Factory Method vs Abstract Factory

## Factory Method

Creates **one product**.

Example:

```python
VehicleFactory → Car / Bike
```

---

## Abstract Factory

Creates **multiple related products**.

Example:

```python
GUIFactory → Button + Menu + Checkbox
```

---

# Quick Checklist

Ask these questions:

### Q1: Do I have multiple product types?

Example:

* Burger
* Garlic Bread

If NO → probably not Abstract Factory.

---

### Q2: Do products belong to families?

Example:

* Singh Family
* King Family

If YES → strong signal.

---

### Q3: Should family products remain compatible?

If YES → use Abstract Factory.

---

# Quick Formula

```text
Multiple Product Types
        +
Multiple Product Families
        +
Family Consistency Required
        =
Abstract Factory Pattern
```
