# Book Scores Smelly Demo

Repo تجريبية مختلفة تمامًا لفحص SonarQube/SonarCloud.

المستهدف:
- Security: قريب من 0 لأن الكود لا يحتوي على exec/eval/secrets/SQL/file deletion/network calls.
- Duplication: عالي جدًا بسبب تكرار منطق التحليل في أكتر من module.
- Code Smells: كتير جدًا: دوال طويلة، شروط متداخلة، magic numbers، أسماء سيئة، dead code، تعقيد عالي، تكرار، TODO/FIXME.
- Coverage: مرفق `coverage.xml` تقريبي بنسبة منخفضة/متوسطة.

تشغيل Sonar:
```bash
sonar-scanner
```
